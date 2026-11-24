param(
    [Parameter(Mandatory = $false)]
    [string]$Destino
)

$ErrorActionPreference = "Stop"

$AvisoPaquete = "El instalador no funciona suelto ni desde la carpeta tlauncher del repositorio. Descarga de Releases el archivo que termina en -tlauncher.zip, extraelo completo y ejecutalo desde esa carpeta extraida."

function Test-NonEmptyString {
    param([object]$Value)
    return ($null -ne $Value -and $Value -is [string] -and -not [string]::IsNullOrWhiteSpace($Value))
}

function Get-ValidChildPath {
    param(
        [string]$Base,
        [string]$Child
    )
    if (-not (Test-NonEmptyString $Base)) {
        throw "La ruta base esta vacia o no es valida."
    }
    if (-not (Test-NonEmptyString $Child)) {
        throw "El nombre de ruta esta vacio o no es valido."
    }
    return Join-Path -Path $Base -ChildPath $Child
}

function Copy-DirectoryContents {
    param(
        [string]$Source,
        [string]$Target
    )
    if (-not (Test-NonEmptyString $Source) -or -not (Test-Path -LiteralPath $Source -PathType Container)) {
        return
    }
    if (-not (Test-NonEmptyString $Target)) {
        throw "La ruta de destino para copiar esta vacia."
    }
    New-Item -ItemType Directory -Path $Target -Force | Out-Null
    Get-ChildItem -LiteralPath $Source -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Target -Recurse -Force
    }
}

try {
    # Resuelve la carpeta del paquete y valida sus piezas antes de cualquier
    # operación de instalación o uso de rutas derivadas.
    $CarpetaPaquete = $PSScriptRoot
    if (-not (Test-NonEmptyString $CarpetaPaquete)) {
        $RutaInvocacion = $MyInvocation.MyCommand.Path
        if (Test-NonEmptyString $RutaInvocacion) {
            $CarpetaPaquete = Split-Path -Parent $RutaInvocacion
        }
    }

    if (-not (Test-NonEmptyString $CarpetaPaquete) -or
        -not (Test-Path -LiteralPath $CarpetaPaquete -PathType Container)) {
        Write-Host $AvisoPaquete -ForegroundColor Red
        exit 1
    }

    $ManifestMods = Get-ValidChildPath -Base $CarpetaPaquete -Child "mods-terceros.json"
    $VersionsPath = Get-ValidChildPath -Base $CarpetaPaquete -Child "versions"
    if (-not (Test-Path -LiteralPath $ManifestMods -PathType Leaf) -or
        -not (Test-Path -LiteralPath $VersionsPath -PathType Container)) {
        Write-Host $AvisoPaquete -ForegroundColor Red
        exit 1
    }

    $Perfiles = @(Get-ChildItem -LiteralPath $VersionsPath -Directory -ErrorAction Stop |
        ForEach-Object {
            $VersionFolder = $_
            if (Test-NonEmptyString $VersionFolder.Name) {
                $ProfileFile = Get-ValidChildPath -Base $VersionFolder.FullName -Child ($VersionFolder.Name + ".json")
                if (Test-Path -LiteralPath $ProfileFile -PathType Leaf) {
                    [PSCustomObject]@{
                        Id = $VersionFolder.Name
                        Directory = $VersionFolder.FullName
                        Profile = $ProfileFile
                    }
                }
            }
        })

    if ($Perfiles.Count -lt 1) {
        Write-Host $AvisoPaquete -ForegroundColor Red
        exit 1
    }

    if (Test-NonEmptyString $Destino) {
        $DestinoMinecraft = $Destino.Trim()
    }
    else {
        $AppData = [Environment]::GetFolderPath("ApplicationData")
        if (-not (Test-NonEmptyString $AppData)) {
            throw "No se pudo obtener la carpeta APPDATA."
        }
        $DestinoMinecraft = Get-ValidChildPath -Base $AppData -Child ".minecraft"
    }

    if (-not (Test-NonEmptyString $DestinoMinecraft) -or
        -not (Test-Path -LiteralPath $DestinoMinecraft -PathType Container)) {
        Write-Host "No existe la carpeta de destino .minecraft: $DestinoMinecraft" -ForegroundColor Red
        Write-Host "No se ha modificado ningun archivo."
        exit 1
    }

    $DestinoMinecraft = (Resolve-Path -LiteralPath $DestinoMinecraft).Path
    $Fecha = Get-Date -Format "yyyyMMdd-HHmmss"
    $Respaldo = Get-ValidChildPath -Base $DestinoMinecraft -Child ("respaldo-modpack-" + $Fecha)
    $ModsDestino = Get-ValidChildPath -Base $DestinoMinecraft -Child "mods"
    $ModsFuente = Get-ValidChildPath -Base $CarpetaPaquete -Child "mods"
    $ConfigDestino = Get-ValidChildPath -Base $DestinoMinecraft -Child "config"
    $ConfigFuente = Get-ValidChildPath -Base $CarpetaPaquete -Child "config"
    $OptionsDestino = Get-ValidChildPath -Base $DestinoMinecraft -Child "options.txt"
    $OptionsFuente = Get-ValidChildPath -Base $CarpetaPaquete -Child "options.txt"
    $VersionsDestino = Get-ValidChildPath -Base $DestinoMinecraft -Child "versions"

    # Se conserva copia de la carpeta de mods previa cuando contiene archivos.
    if (Test-Path -LiteralPath $ModsDestino -PathType Container) {
        $ModsExistentes = @(Get-ChildItem -LiteralPath $ModsDestino -Force -ErrorAction Stop)
        if ($ModsExistentes.Count -gt 0) {
            New-Item -ItemType Directory -Path $Respaldo -Force | Out-Null
            $ModsRespaldo = Get-ValidChildPath -Base $Respaldo -Child "mods"
            Move-Item -LiteralPath $ModsDestino -Destination $ModsRespaldo -Force
        }
    }

    # Respalda options.txt y config existentes antes de reemplazar.
    $HayOptions = Test-Path -LiteralPath $OptionsDestino -PathType Leaf
    $HayConfig = Test-Path -LiteralPath $ConfigDestino -PathType Container
    if ($HayOptions -or $HayConfig) {
        New-Item -ItemType Directory -Path $Respaldo -Force | Out-Null
        if ($HayOptions) {
            $OptionsRespaldo = Get-ValidChildPath -Base $Respaldo -Child "options.txt"
            Copy-Item -LiteralPath $OptionsDestino -Destination $OptionsRespaldo -Force
        }
        if ($HayConfig) {
            $ConfigRespaldo = Get-ValidChildPath -Base $Respaldo -Child "config"
            Copy-DirectoryContents -Source $ConfigDestino -Target $ConfigRespaldo
        }
    }

    # Instala el perfil de Fabric bajo .minecraft/versions/<id>/.
    if (-not (Test-Path -LiteralPath $VersionsDestino -PathType Container)) {
        New-Item -ItemType Directory -Path $VersionsDestino -Force | Out-Null
    }
    foreach ($Perfil in $Perfiles) {
        if (-not (Test-NonEmptyString $Perfil.Id) -or
            -not (Test-NonEmptyString $Perfil.Directory)) {
            throw "Se encontro un perfil de version con datos vacios."
        }
        $VersionIdDestino = Get-ValidChildPath -Base $VersionsDestino -Child $Perfil.Id
        New-Item -ItemType Directory -Path $VersionIdDestino -Force | Out-Null
        Copy-Item -LiteralPath $Perfil.Profile -Destination $VersionIdDestino -Force
    }

    # Copia los JAR propios compilados que contiene el ZIP, si la carpeta existe.
    if (Test-Path -LiteralPath $ModsFuente -PathType Container) {
        if (-not (Test-Path -LiteralPath $ModsDestino -PathType Container)) {
            New-Item -ItemType Directory -Path $ModsDestino -Force | Out-Null
        }
        Get-ChildItem -LiteralPath $ModsFuente -File -Filter "*.jar" |
            Where-Object {
                -not $_.Name.EndsWith("-sources.jar", [StringComparison]::OrdinalIgnoreCase) -and
                -not $_.Name.EndsWith("-dev.jar", [StringComparison]::OrdinalIgnoreCase)
            } |
            ForEach-Object {
                Copy-Item -LiteralPath $_.FullName -Destination $ModsDestino -Force
            }
    }

    # Aplica config y options solo cuando vienen incluidos en el paquete.
    if (Test-Path -LiteralPath $ConfigFuente -PathType Container) {
        Copy-DirectoryContents -Source $ConfigFuente -Target $ConfigDestino
    }
    if (Test-Path -LiteralPath $OptionsFuente -PathType Leaf) {
        Copy-Item -LiteralPath $OptionsFuente -Destination $OptionsDestino -Force
    }

    # Lee y valida la lista de descargas de terceros.
    $ListaMods = Get-Content -LiteralPath $ManifestMods -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($null -eq $ListaMods) {
        throw "El archivo mods-terceros.json esta vacio o no contiene JSON valido: $ManifestMods"
    }
    if ($ListaMods -isnot [System.Array]) {
        $ListaMods = @($ListaMods)
    }

    if (-not (Test-Path -LiteralPath $ModsDestino -PathType Container)) {
        New-Item -ItemType Directory -Path $ModsDestino -Force | Out-Null
    }

    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    }
    catch {
        throw "No se pudo habilitar TLS 1.2 para descargar mods: $($_.Exception.Message)"
    }

    $Descargados = New-Object System.Collections.Generic.List[string]
    $Fallidos = New-Object System.Collections.Generic.List[string]

    foreach ($Mod in $ListaMods) {
        $Nombre = $null
        $Url = $null
        $Sha1 = $null
        if ($null -ne $Mod) {
            $Nombre = $Mod.filename
            $Url = $Mod.url
            $Sha1 = $Mod.sha1
        }

        if (-not (Test-NonEmptyString $Nombre) -or
            -not (Test-NonEmptyString $Url) -or
            -not (Test-NonEmptyString $Sha1)) {
            $Fallidos.Add("Entrada con URL, filename o SHA1 ausente en $ManifestMods")
            continue
        }

        if ($Nombre -match '[/\\:]' -or $Nombre -eq "." -or $Nombre -eq "..") {
            $Fallidos.Add("Nombre de archivo no seguro: $Nombre")
            continue
        }

        $ArchivoDestino = Get-ValidChildPath -Base $ModsDestino -Child $Nombre
        $Correcto = $false
        for ($Intento = 1; $Intento -le 2 -and -not $Correcto; $Intento++) {
            try {
                Invoke-WebRequest -Uri $Url -OutFile $ArchivoDestino -UseBasicParsing -TimeoutSec 120
                $HashActual = (Get-FileHash -LiteralPath $ArchivoDestino -Algorithm SHA1).Hash
                if (-not (Test-NonEmptyString $HashActual) -or
                    $HashActual.ToLowerInvariant() -ne $Sha1.ToLowerInvariant()) {
                    Remove-Item -LiteralPath $ArchivoDestino -Force -ErrorAction SilentlyContinue
                    throw "El SHA1 no coincide para $Nombre"
                }
                $Correcto = $true
                $Descargados.Add($Nombre)
            }
            catch {
                if (Test-Path -LiteralPath $ArchivoDestino -PathType Leaf) {
                    Remove-Item -LiteralPath $ArchivoDestino -Force -ErrorAction SilentlyContinue
                }
                if ($Intento -eq 2) {
                    $Fallidos.Add("$Nombre - $($_.Exception.Message)")
                }
            }
        }
    }

    Write-Host ""
    Write-Host "Instalacion terminada para el perfil: $($Perfiles[0].Id)" -ForegroundColor Green
    Write-Host "Mods de terceros descargados correctamente: $($Descargados.Count)"
    if ($Fallidos.Count -gt 0) {
        Write-Host "Descargas fallidas:" -ForegroundColor Yellow
        foreach ($Fallo in $Fallidos) {
            Write-Host " - $Fallo" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "No hubo descargas fallidas."
    }
    if (Test-Path -LiteralPath $Respaldo -PathType Container) {
        Write-Host "Respaldo creado en: $Respaldo"
    }
    Write-Host ""
    Write-Host "Siguientes pasos:"
    Write-Host "1. Abre TLauncher."
    Write-Host "2. Elige en la lista de versiones: $($Perfiles[0].Id)"
    Write-Host "3. En los ajustes de TLauncher, asigna la memoria recomendada para tu equipo."
    Write-Host "4. Inicia el juego."
    Write-Host "Para volver atras, cierra TLauncher y restaura desde la carpeta de respaldo indicada."
}
catch {
    $RutaError = "(ruta no disponible)"
    if ($_.TargetObject -is [string] -and -not [string]::IsNullOrWhiteSpace($_.TargetObject)) {
        $RutaError = $_.TargetObject
    }
    Write-Host "Fallo la instalacion. Paso o ruta: $RutaError" -ForegroundColor Red
    Write-Host "Detalle: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
