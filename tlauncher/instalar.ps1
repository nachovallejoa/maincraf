param(
    [Parameter(Position = 0)]
    [string]$Destino
)

$ErrorPaquete = "Este instalador no funciona suelto ni desde la carpeta tlauncher del repositorio. Descarga de Releases el archivo que termina en -tlauncher.zip, extraelo COMPLETO y ejecutalo desde esa carpeta extraida."

try {
    $scriptFolder = $PSScriptRoot
    if ([string]::IsNullOrWhiteSpace($scriptFolder)) {
        $scriptPath = $MyInvocation.MyCommand.Path
        if ([string]::IsNullOrWhiteSpace($scriptPath)) {
            throw "No se pudo determinar la ruta del instalador."
        }
        $scriptFolder = Split-Path -Parent $scriptPath
    }
    if ([string]::IsNullOrWhiteSpace($scriptFolder)) {
        throw "No se pudo determinar la carpeta del paquete."
    }

    $thirdPartyManifest = Join-Path -Path $scriptFolder -ChildPath "mods-terceros.json"
    $versionsRoot = Join-Path -Path $scriptFolder -ChildPath "versions"

    if (-not (Test-Path -LiteralPath $thirdPartyManifest -PathType Leaf)) {
        Write-Host $ErrorPaquete -ForegroundColor Yellow
        exit 1
    }
    if (-not (Test-Path -LiteralPath $versionsRoot -PathType Container)) {
        Write-Host $ErrorPaquete -ForegroundColor Yellow
        exit 1
    }

    $versionJsonFiles = @(Get-ChildItem -LiteralPath $versionsRoot -Filter "*.json" -File -Recurse -ErrorAction Stop)
    $validProfile = $null
    foreach ($candidate in $versionJsonFiles) {
        if ($null -eq $candidate -or [string]::IsNullOrWhiteSpace($candidate.FullName)) {
            continue
        }
        $candidateDirectory = Split-Path -Parent $candidate.FullName
        $expectedFile = Join-Path -Path $candidateDirectory -ChildPath ($candidate.BaseName + ".json")
        if ([string]::IsNullOrWhiteSpace($expectedFile)) {
            continue
        }
        if ($candidate.Name -eq ($candidate.BaseName + ".json")) {
            $validProfile = $candidate
            break
        }
    }
    if ($null -eq $validProfile) {
        Write-Host $ErrorPaquete -ForegroundColor Yellow
        exit 1
    }

    if ([string]::IsNullOrWhiteSpace($Destino)) {
        $appData = [Environment]::GetFolderPath("ApplicationData")
        if ([string]::IsNullOrWhiteSpace($appData)) {
            throw "No se pudo determinar la carpeta AppData del usuario."
        }
        $destinationRoot = Join-Path -Path $appData -ChildPath ".minecraft"
    } else {
        $destinationRoot = $Destino.Trim()
    }

    if ([string]::IsNullOrWhiteSpace($destinationRoot)) {
        throw "La ruta de destino esta vacia."
    }
    if (-not (Test-Path -LiteralPath $destinationRoot -PathType Container)) {
        Write-Host "No existe la carpeta destino: $destinationRoot" -ForegroundColor Yellow
        Write-Host "Abre TLauncher una vez o indica una carpeta .minecraft existente como parametro."
        exit 1
    }

    $profileJson = Get-Content -LiteralPath $validProfile.FullName -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop
    $versionId = $profileJson.id
    if ([string]::IsNullOrWhiteSpace($versionId)) {
        throw "El perfil no contiene un id de version en la ruta: $($validProfile.FullName)"
    }
    if ($versionId -match '[\\/:]' -or $versionId -eq "." -or $versionId -eq "..") {
        throw "El id del perfil no es seguro como nombre de carpeta: $versionId"
    }

    $modsSource = Join-Path -Path $scriptFolder -ChildPath "mods"
    $configSource = Join-Path -Path $scriptFolder -ChildPath "config"
    $optionsSource = Join-Path -Path $scriptFolder -ChildPath "options.txt"
    $backupStamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupRoot = Join-Path -Path $destinationRoot -ChildPath ("respaldo-modpack-" + $backupStamp)

    $destinationMods = Join-Path -Path $destinationRoot -ChildPath "mods"
    if (Test-Path -LiteralPath $destinationMods -PathType Container) {
        $existingMods = @(Get-ChildItem -LiteralPath $destinationMods -Force -ErrorAction Stop)
        if ($existingMods.Count -gt 0) {
            New-Item -ItemType Directory -Path $backupRoot -Force -ErrorAction Stop | Out-Null
            $backupMods = Join-Path -Path $backupRoot -ChildPath "mods-anteriores"
            Move-Item -LiteralPath $destinationMods -Destination $backupMods -ErrorAction Stop
        }
    }

    $existingOptions = Join-Path -Path $destinationRoot -ChildPath "options.txt"
    $existingConfig = Join-Path -Path $destinationRoot -ChildPath "config"
    $needsBackup = $false
    if (Test-Path -LiteralPath $existingOptions -PathType Leaf) {
        $needsBackup = $true
    }
    if (Test-Path -LiteralPath $existingConfig -PathType Container) {
        $existingConfigItems = @(Get-ChildItem -LiteralPath $existingConfig -Force -ErrorAction Stop)
        if ($existingConfigItems.Count -gt 0) {
            $needsBackup = $true
        }
    }
    if ($needsBackup -and -not (Test-Path -LiteralPath $backupRoot -PathType Container)) {
        New-Item -ItemType Directory -Path $backupRoot -Force -ErrorAction Stop | Out-Null
    }
    if ((Test-Path -LiteralPath $existingOptions -PathType Leaf) -and -not [string]::IsNullOrWhiteSpace($backupRoot)) {
        Copy-Item -LiteralPath $existingOptions -Destination (Join-Path -Path $backupRoot -ChildPath "options.txt") -Force -ErrorAction Stop
    }
    if ((Test-Path -LiteralPath $existingConfig -PathType Container) -and -not [string]::IsNullOrWhiteSpace($backupRoot)) {
        $existingConfigItems = @(Get-ChildItem -LiteralPath $existingConfig -Force -ErrorAction Stop)
        if ($existingConfigItems.Count -gt 0) {
            Copy-Item -LiteralPath $existingConfig -Destination (Join-Path -Path $backupRoot -ChildPath "config") -Recurse -Force -ErrorAction Stop
        }
    }

    $destinationVersions = Join-Path -Path $destinationRoot -ChildPath "versions"
    if (-not (Test-Path -LiteralPath $destinationVersions -PathType Container)) {
        New-Item -ItemType Directory -Path $destinationVersions -Force -ErrorAction Stop | Out-Null
    }

    $sourceVersionDirectory = Split-Path -Parent $validProfile.FullName
    $destinationVersionDirectory = Join-Path -Path $destinationVersions -ChildPath $versionId
    if (Test-Path -LiteralPath $destinationVersionDirectory -PathType Container) {
        Remove-Item -LiteralPath $destinationVersionDirectory -Recurse -Force -ErrorAction Stop
    }
    Copy-Item -LiteralPath $sourceVersionDirectory -Destination $destinationVersions -Recurse -Force -ErrorAction Stop

    if (Test-Path -LiteralPath $modsSource -PathType Container) {
        $ownModFiles = @(Get-ChildItem -LiteralPath $modsSource -File -Filter "*.jar" -ErrorAction Stop)
        if ($ownModFiles.Count -gt 0) {
            if (-not (Test-Path -LiteralPath $destinationMods -PathType Container)) {
                New-Item -ItemType Directory -Path $destinationMods -Force -ErrorAction Stop | Out-Null
            }
            Copy-Item -LiteralPath (Join-Path -Path $modsSource -ChildPath "*") -Destination $destinationMods -Force -ErrorAction Stop
        }
    }

    if (Test-Path -LiteralPath $configSource -PathType Container) {
        $configItems = @(Get-ChildItem -LiteralPath $configSource -Force -ErrorAction Stop)
        if ($configItems.Count -gt 0) {
            $destinationConfig = Join-Path -Path $destinationRoot -ChildPath "config"
            if (Test-Path -LiteralPath $destinationConfig -PathType Container) {
                Remove-Item -LiteralPath $destinationConfig -Recurse -Force -ErrorAction Stop
            }
            Copy-Item -LiteralPath $configSource -Destination $destinationRoot -Recurse -Force -ErrorAction Stop
        }
    }
    if (Test-Path -LiteralPath $optionsSource -PathType Leaf) {
        if ((Get-Item -LiteralPath $optionsSource -ErrorAction Stop).Length -gt 0) {
            Copy-Item -LiteralPath $optionsSource -Destination (Join-Path -Path $destinationRoot -ChildPath "options.txt") -Force -ErrorAction Stop
        }
    }

    $manifestData = Get-Content -LiteralPath $thirdPartyManifest -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop
    if ($null -eq $manifestData) {
        throw "El manifiesto de mods de terceros esta vacio o no es JSON valido: $thirdPartyManifest"
    }
    if ($manifestData -isnot [System.Array]) {
        $manifestData = @($manifestData)
    }

    if (-not (Test-Path -LiteralPath $destinationMods -PathType Container)) {
        New-Item -ItemType Directory -Path $destinationMods -Force -ErrorAction Stop | Out-Null
    }

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $installedCount = 0
    $failedDownloads = New-Object System.Collections.Generic.List[string]

    foreach ($mod in $manifestData) {
        $url = $mod.url
        $sha1Expected = $mod.sha1
        $fileName = $mod.filename
        $sizeExpected = $mod.size

        if ([string]::IsNullOrWhiteSpace($url) -or
            [string]::IsNullOrWhiteSpace($sha1Expected) -or
            [string]::IsNullOrWhiteSpace($fileName)) {
            $failedDownloads.Add("Entrada incompleta en $thirdPartyManifest")
            continue
        }
        if ($fileName -match '[\\/:]' -or $fileName -eq "." -or $fileName -eq "..") {
            $failedDownloads.Add("Nombre de archivo no seguro: $fileName")
            continue
        }
        if ($sizeExpected -isnot [long] -and $sizeExpected -isnot [int] -and $sizeExpected -isnot [double]) {
            $failedDownloads.Add("Tamano invalido para $fileName")
            continue
        }

        $downloadPath = Join-Path -Path $destinationMods -ChildPath $fileName
        $downloadOk = $false
        for ($attempt = 1; $attempt -le 2; $attempt++) {
            try {
                Invoke-WebRequest -Uri $url -OutFile $downloadPath -UseBasicParsing -TimeoutSec 120 -ErrorAction Stop
                if (-not (Test-Path -LiteralPath $downloadPath -PathType Leaf)) {
                    throw "No se genero el archivo descargado: $downloadPath"
                }
                $actualSize = (Get-Item -LiteralPath $downloadPath -ErrorAction Stop).Length
                if ($actualSize -ne [long]$sizeExpected) {
                    throw "Tamano inesperado en $downloadPath (esperado $sizeExpected, recibido $actualSize)"
                }
                $actualHash = (Get-FileHash -LiteralPath $downloadPath -Algorithm SHA1 -ErrorAction Stop).Hash
                if (-not [string]::Equals($actualHash, $sha1Expected, [StringComparison]::OrdinalIgnoreCase)) {
                    throw "SHA1 incorrecto para $downloadPath"
                }
                $downloadOk = $true
                $installedCount++
                break
            } catch {
                if ($attempt -eq 2) {
                    $failedDownloads.Add("$fileName - $($_.Exception.Message) - ruta: $downloadPath")
                } else {
                    if (Test-Path -LiteralPath $downloadPath -PathType Leaf) {
                        Remove-Item -LiteralPath $downloadPath -Force -ErrorAction SilentlyContinue
                    }
                }
            }
        }
        if (-not $downloadOk -and (Test-Path -LiteralPath $downloadPath -PathType Leaf)) {
            Remove-Item -LiteralPath $downloadPath -Force -ErrorAction SilentlyContinue
        }
    }

    Write-Host ""
    Write-Host "Instalacion terminada." -ForegroundColor Green
    Write-Host "Version instalada: $versionId"
    Write-Host "Mods de terceros descargados y verificados: $installedCount"
    if (Test-Path -LiteralPath $modsSource -PathType Container) {
        Write-Host "Mods propios copiados si estaban incluidos en el paquete."
    }
    if ($needsBackup -or (Test-Path -LiteralPath $backupRoot -PathType Container)) {
        Write-Host "Respaldo creado en: $backupRoot"
    } else {
        Write-Host "No habia mods, config ni options.txt que respaldar."
    }

    if ($failedDownloads.Count -gt 0) {
        Write-Host ""
        Write-Host "Descargas que fallaron:" -ForegroundColor Yellow
        foreach ($failure in $failedDownloads) {
            Write-Host (" - " + $failure) -ForegroundColor Yellow
        }
    } else {
        Write-Host "Todas las descargas de terceros pasaron la verificacion SHA1 y tamano."
    }

    Write-Host ""
    Write-Host "Siguientes pasos:"
    Write-Host "1. Abre TLauncher y elige en la lista de versiones: $versionId"
    Write-Host "2. En los ajustes de TLauncher, configura la memoria recomendada del INSTALL.md."
    Write-Host "3. Inicia el juego."
    Write-Host "Para volver atras, restaura el contenido de la carpeta de respaldo indicada arriba."
} catch {
    $failedPath = ""
    if ($null -ne $_.InvocationInfo -and -not [string]::IsNullOrWhiteSpace($_.InvocationInfo.PSCommandPath)) {
        $failedPath = $_.InvocationInfo.PSCommandPath
    } elseif (-not [string]::IsNullOrWhiteSpace($scriptFolder)) {
        $failedPath = $scriptFolder
    } else {
        $failedPath = "(ruta no disponible)"
    }
    Write-Host "ERROR: fallo el instalador durante un paso de instalacion." -ForegroundColor Red
    Write-Host ("Detalle: " + $_.Exception.Message) -ForegroundColor Red
    Write-Host ("Ruta relacionada: " + $failedPath) -ForegroundColor Red
    exit 1
}
