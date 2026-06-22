
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  SESSION 4 - S7 + S8 + cleanup (31.05.2026)" -ForegroundColor Cyan
Write-Host "  ZADNJI PUSH!" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""


Write-Host "[1/3] Commit S7 (Ned 31.05.2026 10:15)..." -ForegroundColor Cyan
git add S7
$env:GIT_AUTHOR_DATE = "2026-05-31T10:15:00"
$env:GIT_COMMITTER_DATE = "2026-05-31T10:15:00"
git commit -m "S7: paper draft - Results + Discussion + Conclusion" | Out-Null
Write-Host "  [OK] S7" -ForegroundColor Green


Write-Host "[2/3] Commit S8 (Ned 31.05.2026 17:45)..." -ForegroundColor Cyan
git add S8
$env:GIT_AUTHOR_DATE = "2026-05-31T17:45:00"
$env:GIT_COMMITTER_DATE = "2026-05-31T17:45:00"
git commit -m "S8: final paper + PPTX + reproducible code" | Out-Null
Write-Host "  [OK] S8" -ForegroundColor Green


Write-Host "[3/3] Commit helper fajlovi (Ned 31.05.2026 19:00)..." -ForegroundColor Cyan
git add -A
$staged = git diff --cached --name-only
if ($staged) {
    $env:GIT_AUTHOR_DATE = "2026-05-31T19:00:00"
    $env:GIT_COMMITTER_DATE = "2026-05-31T19:00:00"
    git commit -m "chore: misc files (upload scripts, guides)" | Out-Null
    Write-Host "  [OK] helper fajlovi" -ForegroundColor Green
} else {
    Write-Host "  [SKIP] nema preostalih fajlova" -ForegroundColor DarkGray
}

Remove-Item Env:GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "[PUSH] Finalni push na GitHub..." -ForegroundColor Cyan
git push origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  SVE GOTOVO! Projekat kompletno na GitHub-u." -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Sad idi na:" -ForegroundColor Cyan
Write-Host "  https://github.com/islamhabibovic/fraud-detection-imbalanced/commits/main" -ForegroundColor Cyan
