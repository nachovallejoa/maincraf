param(
    [Parameter(Mandatory = $false)]
    [string]$MinecraftDir
)

$ErrorActionPreference = "Stop"

$MissingPackageMessage = @"
Este instalador no funciona suelto ni desde la carpeta tlauncher del repositorio.
Descarga de Releases el archivo que termina en -tlauncher.zip, extraelo completo y ejecuta INSTALAR.bat desde esa carpeta extraida.
"@

try {
    $PackageRoot = $PSScriptRoot
    if ([string]::IsNullOrWhiteSpace($PackageRoot)) {
        $CommandPath = $MyInvocation.MyCommand.Path
        if ([string]::IsNullOrWhiteSpace($CommandPath)) {
            Write-Host $MissingPackageMessage
            exit 1
        }
        $PackageRoot = Split-Path -Parent $CommandPath
    }

    if ([string]::IsNullOrWhiteSpace($PackageRoot)) {
        Write-Host $MissingPackageMessage
        exit 1
    }

    # Antes de cualquier otra operacion, validar que se trata del ZIP completo.
    $ThirdPartyManifest = Join-Path -Path $PackageRoot -ChildPath "mods-terceros.json"
    $VersionsRoot = Join-Path -Path $PackageRoot -ChildPath "versions"

    if ([string]::IsNullOrWhiteSpace($ThirdPartyManifest) -or
        -not (Test-Path -LiteralPath $ThirdPartyManifest -PathType Leaf) -or
        [string]::IsNullOrWhiteSpace($VersionsRoot) -or
        -not (Test-Path -LiteralPath $VersionsRoot -PathType Container)) {
        Write-Host $MissingPackageMessage
        exit 1
    }

    $ProfileFiles = @(Get-ChildItem -LiteralPath $VersionsRoot -Filter "*.json" -File -Recurse)
    $ValidProfiles = @()
    foreach ($ProfileFile in $ProfileFiles) {
        if ($null -eq $ProfileFile -or [string]::IsNullOrWhiteSpace($ProfileFile.FullName)) {
            continue
        }
        if ($ProfileFile.BaseName -eq $ProfileFile.Directory.Name) {
            $ValidProfiles += $ProfileFile
        }
    }
    if ($ValidProfiles.Count -lt 1) {
        Write-Host $MissingPackageMessage
        exit 1
    }

    $ProfileFile = $ValidProfiles[0]
    $VersionId = $ProfileFile.BaseName
    if ([string]::IsNullOrWhiteSpace($VersionId)) {
        throw "El id de version esta vacio en la ruta '$($ProfileFile.FullName)'."
    }

    $ProfileJson = Get-Content -LiteralPath $ProfileFile.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($null -eq $ProfileJson -or [string]::IsNullOrWhiteSpace([string]$ProfileJson.id)) {
        throw "El perfil no contiene un id valido: '$($ProfileFile.FullName)'."
    }
    if ([string]$ProfileJson.id -ne $VersionId) {
        throw "El id del perfil no coincide con su carpeta: '$($ProfileFile.FullName)'."
    }

    if ([string]::IsNullOrWhiteSpace($MinecraftDir)) {
        $AppData = [Environment]::GetFolderPath("ApplicationData")
        if ([string]::IsNullOrWhiteSpace($AppData)) {
            throw "No se pudo determinar la carpeta APPDATA."
        }
        $MinecraftDir = Join-Path -Path $AppData -ChildPath ".minecraft"
    }

    if ([string]::IsNullOrWhiteSpace($MinecraftDir)) {
        throw "La ruta de destino .minecraft esta vacia."
    }
    if (-not (Test-Path -LiteralPath $MinecraftDir -PathType Container)) {
        Write-Host "No existe la carpeta .minecraft de destino: '$MinecraftDir'. No se realizaron cambios."
        exit 1
    }

    $ThirdPartyData = Get-Content -LiteralPath $ThirdPartyManifest -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($null -eq $ThirdPartyData) {
        throw "El archivo de mods de terceros no contiene JSON valido: '$ThirdPartyManifest'."
    }
    if ($ThirdPartyData -isnot [System.Array]) {
        throw "El archivo mods-terceros.json debe contener una lista JSON: '$ThirdPartyManifest'."
    }

    $ModsSource = Join-Path -Path $PackageRoot -ChildPath "mods"
    $ConfigSource = Join-Path -Path $PackageRoot -ChildPath "config"
    $OptionsSource = Join-Path -Path $PackageRoot -ChildPath "options.txt"
    $VersionSource = Join-Path -Path $PackageRoot -ChildPath "versions"
    $OwnModFiles = @()
    if (-not [string]::IsNullOrWhiteSpace($ModsSource) -and
        (Test-Path -LiteralPath $ModsSource -PathType Container)) {
        $OwnModFiles = @(Get-ChildItem -LiteralPath $ModsSource -File -Filter "*.jar")
    }

    $Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    if ([string]::IsNullOrWhiteSpace($Stamp)) {
        throw "No se pudo crear la marca de fecha para el respaldo."
    }
    $BackupDir = Join-Path -Path $MinecraftDir -ChildPath "respaldo-modpack-$Stamp"

    $ExistingMods = Join-Path -Path $MinecraftDir -ChildPath "mods"
    if (-not [string]::IsNullOrWhiteSpace($ExistingMods) -and
        (Test-Path -LiteralPath $ExistingMods -PathType Container)) {
        $ExistingFiles = @(Get-ChildItem -LiteralPath $ExistingMods -Force -Recurse)
        if ($ExistingFiles.Count -gt 0) {
            if ([string]::IsNullOrWhiteSpace($BackupDir)) {
                throw "La ruta del respaldo esta vacia."
            }
            New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
            $BackupMods = Join-Path -Path $BackupDir -ChildPath "mods-anteriores"
            if ([string]::IsNullOrWhiteSpace($BackupMods)) {
                throw "La ruta de respaldo de mods esta vacia."
            }
            Move-Item -LiteralPath $ExistingMods -Destination $BackupMods
        }
    }

    $ExistingOptions = Join-Path -Path $MinecraftDir -ChildPath "options.txt"
    if (-not [string]::IsNullOrWhiteSpace($ExistingOptions) -and
        (Test-Path -LiteralPath $ExistingOptions -PathType Leaf)) {
        if ([string]::IsNullOrWhiteSpace($BackupDir)) {
            throw "La ruta del respaldo esta vacia."
        }
        New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
        Copy-Item -LiteralPath $ExistingOptions -Destination $BackupDir -Force
    }

    $ExistingConfig = Join-Path -Path $MinecraftDir -ChildPath "config"
    if (-not [string]::IsNullOrWhiteSpace($ExistingConfig) -and
        (Test-Path -LiteralPath $ExistingConfig -PathType Container)) {
        if ([string]::IsNullOrWhiteSpace($BackupDir)) {
            throw "La ruta del respaldo esta vacia."
        }
        New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
        $BackupConfig = Join-Path -Path $BackupDir -ChildPath "config"
        if ([string]::IsNullOrWhiteSpace($BackupConfig)) {
            throw "La ruta de respaldo de config esta vacia."
        }
        Copy-Item -LiteralPath $ExistingConfig -Destination $BackupConfig -Recurse -Force
    }

    $DestinationVersions = Join-Path -Path $MinecraftDir -ChildPath "versions"
    $VersionFolderName = $ProfileFile.Directory.Name
    if ([string]::IsNullOrWhiteSpace($VersionFolderName)) {
        throw "La carpeta de version del perfil esta vacia: '$($ProfileFile.FullName)'."
    }
    $VersionSourceFolder = Join-Path -Path $VersionSource -ChildPath $VersionFolderName
    $VersionDestinationFolder = Join-Path -Path $DestinationVersions -ChildPath $VersionFolderName

    if (-not (Test-Path -LiteralPath $VersionSourceFolder -PathType Container)) {
        throw "No existe la carpeta del perfil dentro del paquete: '$VersionSourceFolder'."
    }
    if ([string]::IsNullOrWhiteSpace($DestinationVersions) -or
        [string]::IsNullOrWhiteSpace($VersionDestinationFolder)) {
        throw "La ruta de destino del perfil esta vacia."
    }
    New-Item -ItemType Directory -Path $DestinationVersions -Force | Out-Null
    Copy-Item -LiteralPath $VersionSourceFolder -Destination $DestinationVersions -Recurse -Force

    $InstalledOwnMods = 0
    if ($OwnModFiles.Count -gt 0) {
        $DestinationMods = Join-Path -Path $MinecraftDir -ChildPath "mods"
        if ([string]::IsNullOrWhiteSpace($DestinationMods)) {
            throw "La ruta de destino mods esta vacia."
        }
        New-Item -ItemType Directory -Path $DestinationMods -Force | Out-Null
        foreach ($OwnMod in $OwnModFiles) {
            if ($null -eq $OwnMod -or [string]::IsNullOrWhiteSpace($OwnMod.FullName)) {
                continue
            }
            Copy-Item -LiteralPath $OwnMod.FullName -Destination $DestinationMods -Force
            $InstalledOwnMods++
        }
    }

    $InstalledConfig = $false
    if (-not [string]::IsNullOrWhiteSpace($ConfigSource) -and
        (Test-Path -LiteralPath $ConfigSource -PathType Container)) {
        $ConfigFiles = @(Get-ChildItem -LiteralPath $ConfigSource -Force -Recurse -File)
        if ($ConfigFiles.Count -gt 0) {
            $ConfigDestination = Join-Path -Path $MinecraftDir -ChildPath "config"
            if ([string]::IsNullOrWhiteSpace($ConfigDestination)) {
                throw "La ruta de destino config esta vacia."
            }
            Copy-Item -LiteralPath $ConfigSource -Destination $MinecraftDir -Recurse -Force
            $InstalledConfig = $true
        }
    }

    $InstalledOptions = $false
    if (-not [string]::IsNullOrWhiteSpace($OptionsSource) -and
        (Test-Path -LiteralPath $OptionsSource -PathType Leaf)) {
        $OptionsInfo = Get-Item -LiteralPath $OptionsSource
        if ($null -ne $OptionsInfo -and $OptionsInfo.Length -gt 0) {
            $OptionsDestination = Join-Path -Path $MinecraftDir -ChildPath "options.txt"
            if ([string]::IsNullOrWhiteSpace($OptionsDestination)) {
                throw "La ruta de destino options.txt esta vacia."
            }
            Copy-Item -LiteralPath $OptionsSource -Destination $OptionsDestination -Force
            $InstalledOptions = $true
        }
    }

    $DownloadFailures = New-Object System.Collections.Generic.List[string]
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    $DestinationMods = Join-Path -Path $MinecraftDir -ChildPath "mods"
    if ($ThirdPartyData.Count -gt 0) {
        if ([string]::IsNullOrWhiteSpace($DestinationMods)) {
            throw "La ruta de destino mods esta vacia."
        }
        New-Item -ItemType Directory -Path $DestinationMods -Force | Out-Null
    }

    foreach ($Entry in $ThirdPartyData) {
        try {
            if ($null -eq $Entry) {
                throw "Entrada nula en mods-terceros.json."
            }
            $Url = [string]$Entry.url
            $Hash = [string]$Entry.sha1
            $FileName = [string]$Entry.filename
            $ExpectedSize = $Entry.size

            if ([string]::IsNullOrWhiteSpace($Url) -or
                [string]::IsNullOrWhiteSpace($Hash) -or
                [string]::IsNullOrWhiteSpace($FileName)) {
                throw "Falta URL, SHA1 o nombre de archivo en la entrada del mod."
            }
            if ($Url -notmatch '^https://') {
                throw "La URL no usa HTTPS: '$Url'."
            }
            if ($FileName -match '[\\/]' -or $FileName -match '^\.\.?$') {
                throw "Nombre de archivo no seguro: '$FileName'."
            }
            if ($Hash -notmatch '^[0-9a-fA-F]{40}$') {
                throw "SHA1 no valido para '$FileName'."
            }
            if ($null -eq $ExpectedSize -or [int64]$ExpectedSize -lt 0) {
                throw "Tamano ausente o no valido para '$FileName'."
            }

            $TargetFile = Join-Path -Path $DestinationMods -ChildPath $FileName
            if ([string]::IsNullOrWhiteSpace($TargetFile)) {
                throw "La ruta de descarga esta vacia para '$FileName'."
            }

            $Downloaded = $false
            for ($Attempt = 1; $Attempt -le 2; $Attempt++) {
                try {
                    Invoke-WebRequest -Uri $Url -OutFile $TargetFile -UseBasicParsing -TimeoutSec 120
                    if (-not (Test-Path -LiteralPath $TargetFile -PathType Leaf)) {
                        throw "No se creo el archivo descargado: '$TargetFile'."
                    }
                    $DownloadedInfo = Get-Item -LiteralPath $TargetFile
                    if ($DownloadedInfo.Length -ne [int64]$ExpectedSize) {
                        throw "Tamano incorrecto en '$TargetFile': recibido $($DownloadedInfo.Length), esperado $ExpectedSize."
                    }
                    $ActualHash = (Get-FileHash -LiteralPath $TargetFile -Algorithm SHA1).Hash
                    if ([string]::IsNullOrWhiteSpace($ActualHash) -or
                        $ActualHash.ToLowerInvariant() -ne $Hash.ToLowerInvariant()) {
                        throw "SHA1 incorrecto para '$TargetFile'."
                    }
                    $Downloaded = $true
                    break
                }
                catch {
                    if (Test-Path -LiteralPath $TargetFile -PathType Leaf) {
                        Remove-Item -LiteralPath $TargetFile -Force
                    }
                    if ($Attempt -eq 2) {
                        throw
                    }
                    Start-Sleep -Seconds 2
                }
            }
            if (-not $Downloaded) {
                throw "Descarga fallida para '$FileName'."
            }
        }
        catch {
            $FailureText = "$([string]$Entry.filename): $($_.Exception.Message)"
            [void]$DownloadFailures.Add($FailureText)
        }
    }

    Write-Host ""
    Write-Host "Instalacion terminada."
    Write-Host "Version instalada: $VersionId"
    Write-Host "Mods propios copiados: $InstalledOwnMods"
    Write-Host "Configuracion copiada: $InstalledConfig"
    Write-Host "options.txt copiado: $InstalledOptions"
    if (-not [string]::IsNullOrWhiteSpace($BackupDir) -and
        (Test-Path -LiteralPath $BackupDir -PathType Container)) {
        Write-Host "Respaldo creado en: '$BackupDir'"
    } else {
        Write-Host "No habia mods, config ni options.txt que respaldar."
    }

    if ($DownloadFailures.Count -gt 0) {
        Write-Host ""
        Write-Host "Descargas que fallaron:"
        foreach ($Failure in $DownloadFailures) {
            Write-Host " - $Failure"
        }
    } else {
        Write-Host "Descargas de mods de terceros: correctas."
    }

    Write-Host ""
    Write-Host "Siguientes pasos:"
    Write-Host "1. Abre TLauncher."
    Write-Host "2. Elige en la lista de versiones '$VersionId'."
    Write-Host "3. Ajusta la memoria recomendada en los ajustes de TLauncher."
    Write-Host "4. Inicia el juego."
    Write-Host "Para volver atras, cierra el juego; mueve la carpeta mods instalada fuera de .minecraft y restaura mods-anteriores desde el respaldo si el instalador la creo."
    Write-Host "Restaura tambien config y options.txt desde el respaldo si necesitas recuperar los valores anteriores."
}
catch {
    $FailedPath = $null
    if ($null -ne $_.TargetObject) {
        $FailedPath = [string]$_.TargetObject
    }
    if ([string]::IsNullOrWhiteSpace($FailedPath) -and
        -not [string]::IsNullOrWhiteSpace($MinecraftDir)) {
        $FailedPath = $MinecraftDir
    }
    if ([string]::IsNullOrWhiteSpace($FailedPath)) {
        $FailedPath = "(ruta no disponible)"
    }
    Write-Host "ERROR: fallo el paso de instalacion para la ruta '$FailedPath'. Detalle: $($_.Exception.Message)"
    exit 1
}
