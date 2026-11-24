param(
    [Parameter(Position = 0)]
    [string]$Destino
)

$ErrorActionPreference = "Stop"

function Get-ModpackRoot {
    $candidate = Split-Path -Parent $MyInvocation.MyCommand.Path
    if (-not (Test-Path -LiteralPath (Join-Path $candidate "mods-terceros.json"))) {
        throw "No se encontro mods-terceros.json junto al instalador. Extrae el ZIP completo antes de ejecutar."
    }
    return (Resolve-Path -LiteralPath $candidate).Path
}

function Copy-FilesToDirectory {
    param([string]$Source, [string]$Target)
    if (-not (Test-Path -LiteralPath $Source)) { return }
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    Get-ChildItem -LiteralPath $Source -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Target -Recurse -Force
    }
}

function Test-ModFile {
    param([string]$Path, [string]$ExpectedSha1, [long]$ExpectedSize)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $false }
    $file = Get-Item -LiteralPath $Path
    if ($ExpectedSize -gt 0 -and $file.Length -ne $ExpectedSize) { return $false }
    if ([string]::IsNullOrWhiteSpace($ExpectedSha1)) {
        # [SIN VERIFICAR] Sin hash SHA1, no se considera valida la descarga.
        return $false
    }
    $actual = (Get-FileHash -LiteralPath $Path -Algorithm SHA1).Hash.ToLowerInvariant()
    return ($actual -eq $ExpectedSha1.ToLowerInvariant())
}

try {
    $sourceRoot = Get-ModpackRoot
    if ([string]::IsNullOrWhiteSpace($Destino)) {
        if ([string]::IsNullOrWhiteSpace($env:APPDATA)) {
            throw "No se encontro APPDATA; indica la carpeta .minecraft como parametro."
        }
        $Destino = Join-Path $env:APPDATA ".minecraft"
    }
    $Destino = [System.IO.Path]::GetFullPath([Environment]::ExpandEnvironmentVariables($Destino))
    if (-not (Test-Path -LiteralPath $Destino -PathType Container)) {
        throw "La carpeta de destino no existe: $Destino"
    }

    $versionFolders = @(Get-ChildItem -LiteralPath (Join-Path $sourceRoot "versions") -Directory -ErrorAction SilentlyContinue)
    if ($versionFolders.Count -ne 1) {
        throw "El paquete debe contener exactamente una carpeta de version Fabric en versions/."
    }
    $versionId = $versionFolders[0].Name
    $profileSource = Join-Path $versionFolders[0].FullName ($versionId + ".json")
    if (-not (Test-Path -LiteralPath $profileSource -PathType Leaf)) {
        throw "No se encontro el perfil esperado: versions/$versionId/$versionId.json"
    }

    $backupStamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupPath = Join-Path $Destino ("respaldo-modpack-" + $backupStamp)
    $backupCreated = $false
    $modsPath = Join-Path $Destino "mods"
    $configPath = Join-Path $Destino "config"
    $optionsPath = Join-Path $Destino "options.txt"

    if ((Test-Path -LiteralPath $modsPath -PathType Container) -and
        @(Get-ChildItem -LiteralPath $modsPath -Force).Count -gt 0) {
        New-Item -ItemType Directory -Force -Path $backupPath | Out-Null
        Move-Item -LiteralPath $modsPath -Destination (Join-Path $backupPath "mods")
        $backupCreated = $true
    }
    if (Test-Path -LiteralPath $optionsPath -PathType Leaf) {
        New-Item -ItemType Directory -Force -Path $backupPath | Out-Null
        Copy-Item -LiteralPath $optionsPath -Destination (Join-Path $backupPath "options.txt") -Force
        $backupCreated = $true
    }
    if (Test-Path -LiteralPath $configPath -PathType Container) {
        New-Item -ItemType Directory -Force -Path $backupPath | Out-Null
        Copy-Item -LiteralPath $configPath -Destination (Join-Path $backupPath "config") -Recurse -Force
        $backupCreated = $true
    }

    $versionsTarget = Join-Path $Destino "versions"
    New-Item -ItemType Directory -Force -Path $versionsTarget | Out-Null
    Copy-Item -LiteralPath $versionFolders[0].FullName -Destination $versionsTarget -Recurse -Force
    Copy-FilesToDirectory -Source (Join-Path $sourceRoot "mods") -Target $modsPath
    Copy-FilesToDirectory -Source (Join-Path $sourceRoot "config") -Target $configPath
    $optionsSource = Join-Path $sourceRoot "options.txt"
    if (Test-Path -LiteralPath $optionsSource -PathType Leaf) {
        Copy-Item -LiteralPath $optionsSource -Destination $optionsPath -Force
    }

    New-Item -ItemType Directory -Force -Path $modsPath | Out-Null
    $downloadList = @(Get-Content -LiteralPath (Join-Path $sourceRoot "mods-terceros.json") -Raw -Encoding UTF8 | ConvertFrom-Json)
    $failures = New-Object System.Collections.Generic.List[string]
    $installed = 0
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    foreach ($mod in $downloadList) {
        $filename = [string]$mod.filename
        $url = [string]$mod.url
        if ([string]::IsNullOrWhiteSpace($filename) -or [string]::IsNullOrWhiteSpace($url) -or
            [System.IO.Path]::GetFileName($filename) -ne $filename) {
            $failures.Add("Entrada de descarga invalida")
            continue
        }
        $targetFile = Join-Path $modsPath $filename
        $ok = $false
        for ($attempt = 1; $attempt -le 2; $attempt++) {
            try {
                Invoke-WebRequest -Uri $url -OutFile $targetFile -UseBasicParsing -TimeoutSec 120
                if (Test-ModFile -Path $targetFile -ExpectedSha1 ([string]$mod.sha1) -ExpectedSize ([long]$mod.size)) {
                    $ok = $true
                    break
                }
                Remove-Item -LiteralPath $targetFile -Force -ErrorAction SilentlyContinue
            } catch {
                Remove-Item -LiteralPath $targetFile -Force -ErrorAction SilentlyContinue
            }
        }
        if ($ok) { $installed++ } else { $failures.Add($filename) }
    }

    Write-Host "Instalacion terminada. Version: $versionId"
    Write-Host "Mods de terceros descargados y verificados: $installed"
    if ($backupCreated) { Write-Host "Respaldo creado en: $backupPath" }
    if ($failures.Count -gt 0) {
        Write-Host "Descargas fallidas:"
        $failures | ForEach-Object { Write-Host " - $_" }
        exit 2
    }
    Write-Host "Abre TLauncher y selecciona la version Fabric instalada."
    exit 0
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
    exit 1
}
