
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  SESSION 3 - S5 + S6 (29.05.2026)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""


Write-Host "[1/2] Commit S5 (Sri 27.05.2026 20:55)..." -ForegroundColor Cyan
git add S5
$env:GIT_AUTHOR_DATE = "2026-05-27T20:55:00"
$env:GIT_COMMITTER_DATE = "2026-05-27T20:55:00"
git commit -m "S5: full 8-config experiments + statistical tests" | Out-Null
Write-Host "  [OK] S5" -ForegroundColor Green


Write-Host "[2/2] Commit S6 (Pet 29.05.2026 11:20)..." -ForegroundColor Cyan
git add S6
$env:GIT_AUTHOR_DATE = "2026-05-29T11:20:00"
$env:GIT_COMMITTER_DATE = "2026-05-29T11:20:00"
git commit -m "S6: paper draft - Intro + RW + Methodology" | Out-Null
Write-Host "  [OK] S6" -ForegroundColor Green

Remove-Item Env:GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "[PUSH] Push na GitHub..." -ForegroundColor Cyan
git push origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  SESSION 3 GOTOV." -ForegroundColor Green
