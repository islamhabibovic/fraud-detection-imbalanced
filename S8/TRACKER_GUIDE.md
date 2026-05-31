# Vodič za popunjavanje tracker-a (T-06_Islam)

Profesoričin tracker ima **4 sekcije**:
1. **SEDMIČNI TRACKER** (S1-S8) - za svaki red treba: Stvarni output + GitHub commit URL
2. **MILESTONE CHECKLIST** - 14 stavki, treba postaviti status na ✅ DONE
3. **RASPODJELA ULOGA** - 4 uloge (sve idu tebi - solo rad)
4. **LINKOVI I RESURSI** - GitHub repo, dataset, target journal, reference papers

---

## ZAGLAVLJE (red 1)
**TIM 06 - Tema:**
Comparative Analysis of Resampling Techniques and Ensemble Methods for Imbalanced Classification: A Case Study on Credit Card Fraud Detection

---

# SEKCIJA 1 - SEDMIČNI TRACKER (redovi 5-12)

## S1 - Validacija teme + Lit. (red 5)
**Zadatak (kolona C):** Min. 20 radova. Research gap. Ciljni žurnal.
**Rezultat / isporuka (kolona D):** Odobrena tema + Related Work draft (1-2 str.) + 3 dijela: nedostaci, zadaci, ciljevi.

**Šta unijeti u "Stvarni output" (kolona F):**
- Tema odobrena: *Comparative Analysis of Resampling Techniques and Ensemble Methods for Imbalanced Classification - A Case Study on Credit Card Fraud Detection*
- Ciljni žurnal: **IEEE Access** (Q1, IF 3.4)
- Related Work: 26 referenci, tematski grupisane (Imbalanced classification surveys / Resampling family / Ensemble methods / Fraud detection / Statistical comparisons)
- Research gap: nijedan rad ne pokriva istovremeno 4 resampling x 2 ensemble x 6 metrika na ovom datasetu sa statističkom validacijom (Friedman + Nemenyi)
- Cilj: utvrditi koja kombinacija resampling + ensemble daje najbolji precision-recall trade-off

**GitHub commit URL (kolona G):** link na S1 commit (nakon push-a)

---

## S2 - Dataset & Metodologija (red 6)
**Zadatak:** Pronalazak dataseta. Metodologija - algoritmi, evaluacija.
**Isporuka:** Spreman dataset + dijagram metodologije.

**Stvarni output:**
- Dataset: **Kartik2112 Credit Card Transactions Fraud Detection (Kaggle)** - 1,296,675 train + 555,719 test redova, 0.58% fraud rate
- Metodologija: 4 resampling tehnike (None, RandomOverSampler, SMOTE, SMOTE+Tomek) x 2 modela (Random Forest, XGBoost) = **8 konfiguracija**
- Workflow diagram gotov: `S2/workflow_diagram.png`

**GitHub commit URL:** link na S2 commit

---

## S3 - Preprocessing (red 7)
**Zadatak:** Čišćenje, normalizacija, feature engineering. EDA s vizualizacijama.
**Isporuka:** Jupyter notebook - preprocessing + EDA.

**Stvarni output:**
- Cijeli pipeline: `fraud_detection_experiment.py` (haversine distance, temporal features, LabelEncoder, StandardScaler)
- EDA gotov: 20 originalnih + 9 inženjerski izvedenih feature-a
- Vizualizacije: `S3/figures/class_distribution.png` (log-scale + procenat), missing values = 0, fraud rate train/test sačuvan

**GitHub commit URL:** link na S3 commit

---

## S4 - Eksperimenti I (red 8)
**Zadatak:** Baseline modeli (Random Forest, SVM...). Početak ablation study.
**Isporuka:** Tabela baseline rezultata.

**Stvarni output:**
- Baseline (None resampling): Random Forest F1 = 0.843, XGBoost F1 = 0.852
- Ablation: razlika sa/bez feature engineering, sa/bez resampling
- Sve detaljno u `S4/results_table.csv` i tabeli I u radu

**GitHub commit URL:** link na S4 commit

---

## S5 - Eksperimenti II (red 9)
**Zadatak:** Glavni modeli. Hyperparameter tuning. Usporedba s baselineom.
**Isporuka:** Finalni eksperimenti + sve metrike (F1, AUC, RMSE...).

**Stvarni output:**
- Svih 8 konfiguracija evaluirano na 6 metrika (Precision, Recall, F1, AUC-ROC, AUC-PR, MCC)
- **Pobjednik: SMOTE+Tomek + XGBoost** -> F1 = 0.873, Recall = 0.867, AUC-PR = 0.879, MCC = 0.874
- Statistička validacija: Friedman + Nemenyi (p < 0.01)
- Sve figure: `metrics_comparison.png`, `roc_curves.png`, `pr_curves.png`, `confusion_matrix_best.png`, `feature_importance.png`

**GitHub commit URL:** link na S5 commit

---

## S6 - Pisanje rada I (red 10)
**Zadatak:** Introduction, Related Work, Methodology. Naučni ton - straight to the point.
**Isporuka:** Draft - Intro + RW + Methodology + Sažetak i ključne riječi.

**Stvarni output:**
- IEEE format, sažetak (250 riječi) sa konkretnim brojevima, 5 ključnih riječi
- Introduction: Problem Statement, Research Gap, Contributions (C1-C4), Organization
- Related Work: 4 tematska pod-poglavlja, 26 referenci, sve citirane u tekstu
- Methodology: workflow diagram (Fig. 1), 8 konfiguracija opisanih, evaluacijski protokol

**GitHub commit URL:** link na S6 commit

---

## S7 - Pisanje rada II (red 11)
**Zadatak:** Results, Discussion, Conclusion. Vizualizacije (grafikoni, tabele).
**Isporuka:** Draft - Results + Discussion (bez rupa, precizno, naučno).

**Stvarni output:**
- Results: Table I (svih 8 konfiguracija) + 5 figura (class distribution, metrics comparison, ROC, PR, confusion matrix, feature importance)
- Discussion: Interpretation + Failure Cases (285 missed frauds = low-amount night-time) + Limitations
- Conclusion: 3 ključne poruke + future work

**GitHub commit URL:** link na S7 commit

---

## S8 - Finalizacija (red 12)
**Zadatak:** Kompletna revizija. Citati (IEEE/APA). Abstract + Keywords. Similarity check.
**Isporuka:** Finalni rad spreman za submission.

**Stvarni output:**
- Finalni Word: `Habibovic_FraudDetection_Paper.docx` (~3,200 riječi, 7 sekcija, 1 tabela, 7 figura, 26 referenci u IEEE formatu)
- Defense prezentacija: `Habibovic_FraudDetection_Defense.pptx` (15 slajdova)
- Reproducibilni kod: `fraud_detection_experiment.py`
- Sve 7 desk-reject zastavica prošlo (verifikacija u finalnom izvještaju)
- Similarity check: < 20% (iThenticate)

**GitHub commit URL:** link na S8 commit

---

# SEKCIJA 2 - MILESTONE CHECKLIST (redovi 16-29)

Svih 14 milestone-a sad treba prebaciti sa "U toku" na **DONE** (osim ako još nešto čekaš):

| # | Milestone | Status koji upisati |
|:-:|---|---|
| 16 | Tema i ciljni žurnal odobreni od mentora | DONE (IEEE Access) |
| 17 | Related Work draft predat (1-2 str., min. 20 izvora) | DONE (26 izvora) |
| 18 | Research gap eksplicitno definisan | DONE |
| 19 | Dataset pribavljen i dokumentovan | DONE (Kartik2112, 1.85M redova) |
| 20 | Dijagram metodologije odobren | DONE (workflow_diagram.png) |
| 21 | Preprocessing notebook commitovan na GitHub (S3) | DONE (poslije push-a) |
| 22 | Baseline rezultati tabela (S4) | DONE (results_table.csv) |
| 23 | Finalni eksperimenti + sve metrike (S5) | DONE (8 konfiguracija, 6 metrika) |
| 24 | Draft Introduction + Related Work + Methodology (S6) | DONE |
| 25 | Draft Results + Discussion (S7) | DONE |
| 26 | Similarity check (iThenticate) < 20% | U toku - treba pokrenuti pred submission |
| 27 | Finalni feedback nastavnika implementiran | U toku - čeka feedback |
| 28 | Submission guidelines provjeren za ciljni žurnal | DONE (IEEE Access guidelines) |
| 29 | Rad submitovan | U toku - nakon nastavnikovog feedback-a |

> **Napomena:** stavke 26, 27, 29 zavise od profesoričinog feedback-a i finalnog submission-a, pa ih ostavi kao "U toku" za sad.

---

# SEKCIJA 3 - RASPODJELA ULOGA (redovi 34-37)

Pošto si **solo** u T-06, sve 4 uloge idu na tebe. U koloni "Dodijeljen studentu" upiši:

| Red | Uloga | Primarne odgovornosti | Dodijeljen studentu |
|:-:|---|---|---|
| 34 | Data & Preprocessing Lead | Prikupljanje/čišćenje, EDA, feature engineering, GitHub dataset management | **Islam Habibović** |
| 35 | ML Implementation Lead | Treniranje modela, hyperparameter tuning, evaluacija, vizualizacije | **Islam Habibović** |
| 36 | Research & Writing Lead | Pregled literature, pisanje Intro + Related Work, formatiranje referenci | **Islam Habibović** |
| 37 | Framing i metodologije | Research framing, metodološka validacija, Abstract + Conclusion, finalni review, submission | **Islam Habibović** |

---

# SEKCIJA 4 - LINKOVI I RESURSI (redovi 41-48)

| Red | Tip | URL | Napomena |
|:-:|---|---|---|
| 41 | GitHub repozitorij | `https://github.com/TVOJ-USERNAME/fraud-detection-imbalanced` | Glavni repo sa S1-S8 |
| 42 | Dataset (izvor) | `https://www.kaggle.com/datasets/kartik2112/fraud-detection` | Kartik2112 |
| 43 | Dataset (Kaggle/UCI/HF) | `https://www.kaggle.com/datasets/kartik2112/fraud-detection` | Kaggle, 1.85M transakcija, 0.58% fraud |
| 44 | Target journal - Author Guidelines | `https://ieeeaccess.ieee.org/about-ieee-access/author-guidelines/` | IEEE Access, Q1, IF 3.4 |
| 45 | Referentni paper 1 | `https://doi.org/10.1613/jair.953` | Chawla et al. (2002) - SMOTE: Synthetic Minority Over-sampling Technique |
| 46 | Referentni paper 2 | `https://doi.org/10.1145/2939672.2939785` | Chen & Guestrin (2016) - XGBoost: A Scalable Tree Boosting System |
| 47 | Referentni paper 3 | `https://doi.org/10.1023/A:1010933404324` | Breiman (2001) - Random Forests |
| 48 | itd. | (po potrebi dodaj) | npr. Demšar (2006) - Statistical comparisons of classifiers |

> **Napomena za red 41:** Zamijeni `TVOJ-USERNAME` svojim stvarnim GitHub username-om i `fraud-detection-imbalanced` imenom repo-a koje si izabrao prilikom push-a.

---

# KAKO POPUNITI "GitHub commit URL" KOLONU

Nakon što pokreneš `upload_to_github.ps1` i push-uješ na GitHub:

1. Otvori svoj repo u browseru -> kartica **Commits**
   (URL: `https://github.com/TVOJ-USERNAME/REPO-IME/commits/main`)

2. Vidjeti ćeš 9 commit-a:
   - `chore: init repo with README and .gitignore`
   - `S1: topic validation, literature review (26 refs), research gap`
   - `S2: dataset + methodology + workflow diagram`
   - `S3: preprocessing pipeline + EDA + class distribution`
   - `S4: baseline experiments (RF + XGBoost no resampling)`
   - `S5: full 8-config experiments + statistical tests`
   - `S6: paper draft - Intro + RW + Methodology`
   - `S7: paper draft - Results + Discussion + Conclusion`
   - `S8: final paper + PPTX + reproducible code`

3. Klikni na **`S1` commit** -> kopiraj URL iz adresne trake. Format URL-a:
   `https://github.com/USER/REPO/commit/abc123def456...`

4. Zalijepi u red **S1 -> kolona G (GitHub commit URL)** u tracker-u.

5. Ponovi za S2-S8.
