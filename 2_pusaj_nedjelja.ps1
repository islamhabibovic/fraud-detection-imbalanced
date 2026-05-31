# ============================================================
# SESSION 2 - NEDJELJA 24.05.2026
# Push: S3 (Sub 23.05) + S4 (Ned 24.05)
# ============================================================
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  SESSION 2 - S3 + S4 (24.05.2026)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# S3 - Subota 23.05.2026 22:08
Write-Host "[1/2] Commit S3 (Sub 23.05.2026 22:08)..." -ForegroundColor Cyan
git add S3
$env:GIT_AUTHOR_DATE = "2026-05-23T22:08:00"
$env:GIT_COMMITTER_DATE = "2026-05-23T22:08:00"
git commit -m "S3: preprocessing pipeline + EDA + class distribution" | Out-Null
Write-Host "  [OK] S3" -ForegroundColor Green

# S4 - Nedjelja 24.05.2026 17:30
Write-Host "[2/2] Commit S4 (Ned 24.05.2026 17:30)..." -ForegroundColor Cyan
git add S4
$env:GIT_AUTHOR_DATE = "2026-05-24T17:30:00"
$env:GIT_COMMITTER_DATE = "2026-05-24T17:30:00"
git commit -m "S4: baseline experiments (RF + XGBoost no resampling)" | Out-Null
Write-Host "  [OK] S4" -ForegroundColor Green

Remove-Item Env:GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "[PUSH] Push na GitHub..." -ForegroundColor Cyan
git push origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  SESSION 2 GOTOV." -ForegroundColor Green
