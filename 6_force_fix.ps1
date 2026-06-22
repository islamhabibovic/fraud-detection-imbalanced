
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===========================================" -ForegroundColor Yellow
Write-Host "  FORCE FIX: S6 + S7 sa bosanskom verzijom" -ForegroundColor Yellow
Write-Host "===========================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "OVO ce force push-ovati novu historiju." -ForegroundColor Yellow
Write-Host "S1-S5 commitovi ostaju isti." -ForegroundColor Yellow
Write-Host "S6, S7, S8 i helper commitovi dobijaju nove hash-eve." -ForegroundColor Yellow
Write-Host "Moras ponovo kopirati URL-ove za S6, S7, S8 u tracker." -ForegroundColor Yellow
Write-Host ""
$confirm = Read-Host "Nastaviti? (da/ne)"
if ($confirm -ne "da") { Write-Host "Otkazano."; exit 0 }


Write-Host ""
Write-Host "[1/7] Pronalazim S5 commit hash..." -ForegroundColor Cyan
$s5Hash = git log --grep="^S5:" --format="%H" | Select-Object -First 1
if (-not $s5Hash) {
    Write-Host "  [GRESKA] S5 commit nije pronadjen!" -ForegroundColor Red
    exit 1
}
Write-Host "  [OK] S5 = $s5Hash" -ForegroundColor Green


Write-Host ""
Write-Host "[2/7] Reset historija na S5 (cuvam fajlove)..." -ForegroundColor Cyan
git reset --mixed $s5Hash
Write-Host "  [OK] HEAD je sad na S5" -ForegroundColor Green


Write-Host ""
Write-Host "[3/7] Commit S6 (Pet 29.05.2026 11:20) - sa BS docx..." -ForegroundColor Cyan
git add S6
$env:GIT_AUTHOR_DATE = "2026-05-29T11:20:00"
$env:GIT_COMMITTER_DATE = "2026-05-29T11:20:00"
git commit -m "S6: paper draft - Intro + RW + Methodology" | Out-Null
Write-Host "  [OK] S6" -ForegroundColor Green


Write-Host ""
Write-Host "[4/7] Commit S7 (Ned 31.05.2026 10:15) - sa BS docx..." -ForegroundColor Cyan
git add S7
$env:GIT_AUTHOR_DATE = "2026-05-31T10:15:00"
$env:GIT_COMMITTER_DATE = "2026-05-31T10:15:00"
git commit -m "S7: paper draft - Results + Discussion + Conclusion" | Out-Null
Write-Host "  [OK] S7" -ForegroundColor Green


Write-Host ""
Write-Host "[5/7] Commit S8 (Ned 31.05.2026 17:45)..." -ForegroundColor Cyan
git add S8
$env:GIT_AUTHOR_DATE = "2026-05-31T17:45:00"
$env:GIT_COMMITTER_DATE = "2026-05-31T17:45:00"
git commit -m "S8: final paper + PPTX + reproducible code" | Out-Null
Write-Host "  [OK] S8" -ForegroundColor Green


Write-Host ""
Write-Host "[6/7] Commit helper fajlovi (Ned 31.05.2026 19:00)..." -ForegroundColor Cyan
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
Write-Host "[7/7] FORCE PUSH na GitHub..." -ForegroundColor Cyan
git push -f origin main

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  GOTOVO! S6, S7, S8 i helper imaju nove hash-eve." -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Sad idi na:" -ForegroundColor Cyan
Write-Host "  https://github.com/islamhabibovic/fraud-detection-imbalanced/commits/main" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Kopiraj nove URL-ove u tracker:" -ForegroundColor Cyan
Write-Host "  S6 commit -> G10 (red 10)" -ForegroundColor Cyan
Write-Host "  S7 commit -> G11 (red 11)" -ForegroundColor Cyan
Write-Host "  S8 commit -> G12 (red 12)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
