
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Projekat T-06 Islam - GitHub Upload" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""


try {
    $gitVersion = git --version
    Write-Host "[OK] $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Git nije instaliran." -ForegroundColor Red
    Write-Host "Preuzmi sa: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}


Write-Host ""
Write-Host "PRIJE NEGO POKRENES:" -ForegroundColor Yellow
Write-Host "  1) Idi na https://github.com/new"
Write-Host "  2) Ime repo-a (predlog): fraud-detection-imbalanced"
Write-Host "  3) Odaberi 'Private' (preporuceno za sad)"
Write-Host "  4) NE biraj 'Add a README' (vec ga imamo)"
Write-Host "  5) Klikni 'Create repository'"
Write-Host "  6) Kopiraj HTTPS URL (npr. https://github.com/USER/fraud-detection-imbalanced.git)"
Write-Host ""

$repoUrl = Read-Host "Zalijepi GitHub repo HTTPS URL"
if ([string]::IsNullOrWhiteSpace($repoUrl)) {
    Write-Host "[ERROR] URL je prazan, izlazim." -ForegroundColor Red
    exit 1
}


$existingName  = git config --global user.name  2>$null
$existingEmail = git config --global user.email 2>$null

if (-not $existingName) {
    $name = Read-Host "Tvoje puno ime za git (npr. Islam Habibovic)"
    git config --global user.name $name
}
if (-not $existingEmail) {
    git config --global user.email "islamhabibovic89@gmail.com"
}

Write-Host ""
Write-Host "[OK] Git identitet:" -ForegroundColor Green
Write-Host "     $(git config --global user.name) <$(git config --global user.email)>"


Write-Host ""
Write-Host "[KORAK 1/3] Inicijalizujem git repozitorij..." -ForegroundColor Cyan
if (-not (Test-Path ".git")) {
    git init
    git branch -M main
}


Write-Host ""
Write-Host "[KORAK 2/3] Pravim 8 commitova (S1-S8)..." -ForegroundColor Cyan

function Add-PhaseCommit {
    param([string]$Path, [string]$Message)

    if (Test-Path $Path) {
        git add $Path
      
        $staged = git diff --cached --name-only
        if ($staged) {
            git commit -m $Message
            Write-Host "  [OK] $Message" -ForegroundColor Green
        } else {
            Write-Host "  [SKIP] $Path - nema promjena" -ForegroundColor DarkGray
        }
    } else {
        Write-Host "  [SKIP] $Path - folder ne postoji" -ForegroundColor DarkGray
    }
}


git add README.md .gitignore
git commit -m "chore: init repo with README and .gitignore"

Add-PhaseCommit "S1" "S1: topic validation, literature review (26 refs), research gap"
Add-PhaseCommit "S2" "S2: dataset + methodology + workflow diagram"
Add-PhaseCommit "S3" "S3: preprocessing pipeline + EDA + class distribution"
Add-PhaseCommit "S4" "S4: baseline experiments (RF + XGBoost no resampling)"
Add-PhaseCommit "S5" "S5: full 8-config experiments + statistical tests"
Add-PhaseCommit "S6" "S6: paper draft - Intro + RW + Methodology"
Add-PhaseCommit "S7" "S7: paper draft - Results + Discussion + Conclusion"
Add-PhaseCommit "S8" "S8: final paper + PPTX + reproducible code"


git add -A
$leftover = git diff --cached --name-only
if ($leftover) {
    git commit -m "chore: misc files (upload script, guides)"
}


Write-Host ""
Write-Host "[KORAK 3/3] Push na GitHub..." -ForegroundColor Cyan


$remoteExists = git remote 2>$null | Select-String "^origin$"
if ($remoteExists) {
    git remote set-url origin $repoUrl
} else {
    git remote add origin $repoUrl
}

Write-Host ""
Write-Host "Sad ce te git pitati za GitHub username i password." -ForegroundColor Yellow
Write-Host "Password = Personal Access Token (NE tvoja GitHub lozinka)." -ForegroundColor Yellow
Write-Host "Token napravi na: https://github.com/settings/tokens/new" -ForegroundColor Yellow
Write-Host "  - Scope: oznaci 'repo'" -ForegroundColor Yellow
Write-Host "  - Expiration: 90 days je OK" -ForegroundColor Yellow
Write-Host ""

git push -u origin main
