# Kako postaviti projekat na GitHub (S1-S8)

Vodic korak po korak. Postoje dvije opcije: **automatska** (preporuceno) i **rucna**.

---

## Opcija A - AUTOMATSKA (preporuceno)

Skripta `upload_to_github.ps1` radi sve za tebe: inicijalizuje repo, pravi 8
commitova (po jedan za svaki S1-S8), dodaje remote i push-uje na GitHub.

### Preduslov 1: Instaliraj Git (ako nemas)
- Preuzmi sa https://git-scm.com/download/win
- Tokom instalacije ostavi sve **default** opcije i klikni Next do kraja.
- Provjera: otvori PowerShell i ukucaj `git --version`. Treba da pise nesto kao
  `git version 2.45.0.windows.1`.

### Preduslov 2: GitHub nalog + repo
1. Idi na https://github.com/new (uloguj se ako vec nisi).
2. Repository name: `fraud-detection-imbalanced` (ili kako god zelis).
3. **Privacy: Private** (preporuceno za sad - mozes uvijek kasnije prebaciti na Public).
4. **NE** stikliraj "Add a README file" - vec ga imamo.
5. **NE** dodavaj .gitignore ili license - vec ih imamo.
6. Klikni **Create repository**.
7. Na sljedecoj stranici, kopiraj HTTPS URL koji izgleda ovako:
   `https://github.com/TVOJ-USERNAME/fraud-detection-imbalanced.git`

### Preduslov 3: Personal Access Token (umjesto GitHub lozinke)
GitHub vise ne dozvoljava push sa obicnom lozinkom. Treba ti token:
1. Idi na https://github.com/settings/tokens/new
2. **Note:** "Projekat T-06 push"
3. **Expiration:** 90 days
4. **Scopes:** stikliraj `repo` (cijeli blok)
5. Klikni **Generate token**
6. **Kopiraj token ODMAH** (vidi se samo jednom!) - sacuvaj ga u Notes/Notepad
   privremeno. Pocinje sa `ghp_...`

### Pokretanje skripte
1. Otvori folder `C:\Users\islam\Desktop\Projekat_FraudDetection_T06_Islam`
2. Drzi **Shift** i desnim klikom mis-em u prazan prostor unutar foldera.
3. Klikni **"Open PowerShell window here"** (ili **"Open in Terminal"**).
4. Ukucaj:
   ```powershell
   .\upload_to_github.ps1
   ```
5. Ako PowerShell odbije sa porukom o "execution policy", pokreni jednom:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
   ...i potvrdi sa **Y**, pa pokreni skriptu ponovo.
6. Kad te skripta pita:
   - Repo URL -> zalijepi onaj iz Preduslova 2
   - Username -> tvoj GitHub username
   - Password -> **TOKEN** iz Preduslova 3 (NE tvoja GitHub lozinka!)
7. Sacekaj. Trebalo bi da vidis **"GOTOVO! Projekat je na GitHub-u."**

### Sta dalje?
- Otvori repo u browseru i provjeri da li su svi folderi tu (S1-S8 + README).
- Idi na karticu **Commits** - vidjeces 8 commit-a po fazama plus inicijalni
  `chore: init repo`. Klikni na svaki S1-S8 commit, kopiraj URL iz adresne
  trake i nalijepi u kolonu **"GitHub commit URL"** u profesoricinom trackeru.

---

## Opcija B - RUCNI redoslijed komandi (ako ne zelis skriptu)

Otvori PowerShell u folderu `Projekat_FraudDetection_T06_Islam` i ukucaj redom:

```powershell
# 1) Init
git init
git branch -M main
git config user.name "Islam Habibovic"
git config user.email "islamhabibovic89@gmail.com"

# 2) Inicijalni commit (root fajlovi)
git add README.md .gitignore
git commit -m "chore: init repo with README and .gitignore"

# 3) Osam faznih commitova
git add S1; git commit -m "S1: topic validation, literature review (26 refs), research gap"
git add S2; git commit -m "S2: dataset + methodology + workflow diagram"
git add S3; git commit -m "S3: preprocessing pipeline + EDA + class distribution"
git add S4; git commit -m "S4: baseline experiments (RF + XGBoost no resampling)"
git add S5; git commit -m "S5: full 8-config experiments + statistical tests"
git add S6; git commit -m "S6: paper draft - Intro + RW + Methodology"
git add S7; git commit -m "S7: paper draft - Results + Discussion + Conclusion"
git add S8; git commit -m "S8: final paper + PPTX + reproducible code"

# 4) Pokupi sve preostalo
git add -A
git commit -m "chore: misc files (upload script, guides)"

# 5) Push (zamijeni URL svojim)
git remote add origin https://github.com/TVOJ-USERNAME/fraud-detection-imbalanced.git
git push -u origin main
```

Kad ti git zatrazi password -> nalijepi **Personal Access Token**, ne lozinku.

---

## Opcija C - Web upload (najjednostavnije, ali bez S1-S8 commit istorije)

Ako ne zelis instalirati git uopste:
1. Napravi repo na https://github.com/new (kao u Opciji A).
2. Na stranici repo-a klikni **"uploading an existing file"**.
3. Drag-and-drop **cijeli folder** `Projekat_FraudDetection_T06_Islam`.
4. Commit message: `Initial commit - kompletan projekat S1-S8`
5. Klikni **Commit changes**.

**Mana ove opcije:** Imaces samo jedan commit, ne 8 odvojenih po fazama.
Profesorica trazi po jedan **GitHub commit URL** za svaku sedmicu, pa ce ti
sve kolone imati isti URL. Za TRACKER svrhe Opcija A/B je bolja.

---

## Sta ako napravim gresku?

**Greska: `fatal: not a git repository`**
- Otvorio si PowerShell u pogresnom folderu. `cd` u
  `C:\Users\islam\Desktop\Projekat_FraudDetection_T06_Islam`.

**Greska: `Authentication failed`**
- Koristis obicnu lozinku umjesto Personal Access Tokena. Vrati se na
  Preduslov 3 u Opciji A.

**Greska: `Updates were rejected`**
- Repo na GitHub-u vec ima fajlove (vjerovatno si dodao README pri kreiranju).
  Pokreni: `git pull origin main --allow-unrelated-histories` pa onda
  `git push -u origin main`.

**Zelim ponovo napraviti repo iz pocetka**
- Obrisi `.git` folder unutar projekta (`Remove-Item -Recurse -Force .git`)
  i pokreni `upload_to_github.ps1` ponovo.

---

## Tracker - kako popuniti "GitHub commit URL" kolonu

Nakon push-a:
1. Otvori svoj repo u browseru -> kartica **Commits** (ili direktno
   `https://github.com/USER/repo/commits/main`).
2. Vidjet ces 8 commit-a + inicijalni:
   - `S8: final paper + PPTX + reproducible code`
   - `S7: paper draft - Results + Discussion + Conclusion`
   - `S6: paper draft - Intro + RW + Methodology`
   - `S5: full 8-config experiments + statistical tests`
   - `S4: baseline experiments (RF + XGBoost no resampling)`
   - `S3: preprocessing pipeline + EDA + class distribution`
   - `S2: dataset + methodology + workflow diagram`
   - `S1: topic validation, literature review (26 refs), research gap`
   - `chore: init repo with README and .gitignore`
3. Klikni na **`S1` commit** -> kopiraj URL iz adresne trake
   (izgleda ovako: `https://github.com/USER/repo/commit/abc123...`)
4. Zalijepi u red **S1 -> kolona GitHub commit URL** u tracker-u.
5. Ponovi za S2-S8.
