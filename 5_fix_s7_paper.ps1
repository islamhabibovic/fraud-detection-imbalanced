
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  FIX: S7 paper draft (31.05.2026)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""


Write-Host "[1/1] Commit fix S7 paper (Ned 31.05.2026 19:30)..." -ForegroundColor Cyan
git add S7/Habibovic_FraudDetection_Paper.docx
$env:GIT_AUTHOR_DATE = "2026-05-31T19:30:00"
$env:GIT_COMMITTER_DATE = "2026-05-31T19:30:00"
git commit -m "fix: align S7 paper draft with final affiliation" | Out-Null
Write-Host "  [OK] fix commit" -ForegroundColor Green

Remove-Item Env:GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "[PUSH] Push na GitHub..." -ForegroundColor Cyan
git push origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  S7 paper draft popravljen i push-ovan." -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
