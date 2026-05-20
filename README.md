# Comparative Analysis of Resampling Techniques and Ensemble Methods for Imbalanced Classification

> A Case Study on Credit-Card Fraud Detection

![Status](https://img.shields.io/badge/status-final-success)
![Course](https://img.shields.io/badge/course-Data%20Mining-blue)
![Semester](https://img.shields.io/badge/semester-Summer%202026-orange)
![Team](https://img.shields.io/badge/team-T--06-purple)

**Autor:** Islam Habibovic
**Mentori:** doc. dr. Adnan Dzelihodzic - as. mr. Narcisa Hadzajlic - mr. Faris Hambo
**Kurs:** Rudarenje podataka, ljetni semestar 2026
**Institucija:** Internacionalni univerzitet u Sarajevu (IUS)

---

## TL;DR

Uporedna analiza 4 resampling tehnike (None, Random Over-Sampling, SMOTE, SMOTE+Tomek)
i 2 ensemble modela (Random Forest, XGBoost) na Kartik2112 credit-card fraud detection
datasetu (1.85M transakcija, 0.58% fraud rate). Evaluirano kroz 6 metrika sa
statistickom validacijom (Friedman + Nemenyi post-hoc test).

**Najbolji rezultat:** SMOTE+Tomek + XGBoost -> F1 = **0.873**, AUC-PR = **0.879**, MCC = **0.874**.

---

## Struktura repozitorija

Svaki folder `S1` - `S8` odgovara jednoj fazi iz profesoricinog tracker-a (T-06_Islam).
U svakom folderu se nalazi `Sx_README.txt` sa tacnim tekstom za kolonu "Stvarni output"
u tracker-u, plus relevantne datoteke za tu fazu.

| Folder | Faza                        | Glavni outputi                                      |
|:------:|-----------------------------|-----------------------------------------------------|
| S1     | Validacija teme + Lit.      | tema, ciljni zurnal, research gap, 26 referenci     |
| S2     | Dataset & Metodologija      | workflow diagram, EDA stats                         |
| S3     | Preprocessing               | Python pipeline, class distribution                 |
| S4     | Eksperimenti I              | baseline results CSV                                |
| S5     | Eksperimenti II             | sve 8 konfiguracija + 5 figura                      |
| S6     | Pisanje rada I              | Word draft (Intro + RW + Methodology)               |
| S7     | Pisanje rada II             | Word draft (Results + Discussion + Conclusion)      |
| S8     | Finalizacija                | finalni rad + PPTX + reproducibilni kod             |

---

## Glavni deliverables (folder `S8/`)

1. **`Habibovic_FraudDetection_Paper.docx`** - finalni naucni rad u IEEE formatu (~3200 rijeci, 7 sekcija, 1 tabela, 7 figura, 26 referenci)
2. **`Habibovic_FraudDetection_Defense.pptx`** - 15-slide defense prezentacija
3. **`fraud_detection_experiment.py`** - reproducibilni eksperimentalni kod
4. **`TRACKER_GUIDE.md`** - sta tacno upisati u svaki red profesoricinog tracker-a

---

## Kljucni rezultati

| Konfiguracija            | Precision | Recall | F1        | AUC-ROC | AUC-PR    | MCC       |
|--------------------------|-----------|--------|-----------|---------|-----------|-----------|
| Baseline RF              | 0.851     | 0.836  | 0.843     | 0.978   | 0.838     | 0.851     |
| Baseline XGBoost         | 0.859     | 0.846  | 0.852     | 0.981   | 0.857     | 0.856     |
| **SMOTE+Tomek XGBoost**  | **0.879** | **0.867** | **0.873** | **0.987** | **0.879** | **0.874** |

Razlika izmedju najboljeg modela i baseline-a je statisticki znacajna
(Friedman + Nemenyi, p < 0.01).

---

## Dataset

**Kartik2112 - Credit Card Transactions Fraud Detection** (Kaggle)
- Link: https://www.kaggle.com/datasets/kartik2112/fraud-detection
- Train: 1,296,675 transakcija (0.58% fraud)
- Test:  555,719 transakcija (0.39% fraud)
- 23 originalna feature-a + 9 inzenjerski izvedenih (haversine distance, temporal features)

> Napomena: CSV fajlovi nisu u repo-u (preveliki) - preuzeti sa Kaggle linka iznad.

---

## Reprodukcija

```bash
# 1) Instalacija dependency-ja
pip install -r requirements.txt

# 2) Preuzmi dataset sa Kaggle linka iznad u folder ./data/

# 3) Pokreni eksperimente (zadnjih 8 konfiguracija)
python S8/fraud_detection_experiment.py
```

---

## Citiranje

Ako koristis ovaj rad ili kod, molim te citiraj:

```
Habibovic, I. (2026). Comparative Analysis of Resampling Techniques
and Ensemble Methods for Imbalanced Classification: A Case Study
on Credit-Card Fraud Detection. Data Mining course project,
International University of Sarajevo.
```

---

## License

MIT License - za akademske svrhe. Dataset zadrzava svoju originalnu licencu (Kaggle).
