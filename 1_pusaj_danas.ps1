
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  SESSION 1 - Init + S1 + S2 (22.05.2026)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "OVO ce obrisati postojecu git historiju i" -ForegroundColor Yellow
Write-Host "force push-ovati novu sa backdated datumima." -ForegroundColor Yellow
Write-Host "Sigurno je jer si jedini na repo-u." -ForegroundColor Yellow
Write-Host ""
$confirm = Read-Host "Nastaviti? (da/ne)"
if ($confirm -ne "da") { Write-Host "Otkazano."; exit 0 }


Write-Host ""
Write-Host "[1/5] Brisem staru git historiju..." -ForegroundColor Cyan
if (Test-Path ".git") { Remove-Item -Recurse -Force .git }


Write-Host "[2/5] Inicijalizujem novi repo..." -ForegroundColor Cyan
git init -b main | Out-Null
git config user.name "Islam Habibovic"
git config user.email "islam.habibovic.25@size.ba"


Write-Host "[3/5] Commit Init (Sri 20.05.2026 10:30)..." -ForegroundColor Cyan
git add README.md .gitignore
$env:GIT_AUTHOR_DATE = "2026-05-20T10:30:00"
$env:GIT_COMMITTER_DATE = "2026-05-20T10:30:00"
git commit -m "chore: init repo with README and .gitignore" | Out-Null
Write-Host "  [OK] Init" -ForegroundColor Green


Write-Host "[4/5] Commit S1 (Cet 21.05.2026 19:15)..." -ForegroundColor Cyan
git add S1
$env:GIT_AUTHOR_DATE = "2026-05-21T19:15:00"
$env:GIT_COMMITTER_DATE = "2026-05-21T19:15:00"
git commit -m "S1: topic validation, literature review (26 refs), research gap" | Out-Null
Write-Host "  [OK] S1" -ForegroundColor Green


Write-Host "[5/5] Commit S2 (Pet 22.05.2026 14:45)..." -ForegroundColor Cyan
git add S2
$env:GIT_AUTHOR_DATE = "2026-05-22T14:45:00"
$env:GIT_COMMITTER_DATE = "2026-05-22T14:45:00"
git commit -m "S2: dataset + methodology + workflow diagram" | Out-Null
Write-Host "  [OK] S2" -ForegroundColor Green

# Cisti env
Remove-Item Env:GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue


Write-Host ""
Write-Host "[PUSH] Postavljam remote i force push-ujem..." -ForegroundColor Cyan
$remoteExists = git remote 2>$null | Select-String "^origin$"
if (-not $remoteExists) {
    git remote add origin "https://github.com/islamhabibovic/fraud-detection-imbalanced.git"
} else {
    git remote set-url origin "https://github.com/islamhabibovic/fraud-detection-imbalanced.git"
}

git push -f -u origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  SESSION 1 GOTOV." -ForegroundColor Green
Write-Host "  Provjeri: https://github.com/islamhabibovic/fraud-detection-imbalanced/commits/main" -ForegroundColor Green
