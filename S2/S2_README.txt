S2 - Dataset & Metodologija

ZADATAK:  Pronalazak dataseta, metodologija (algoritmi, evaluacija).
ISPORUKA: Spreman dataset + dijagram metodologije.

DATASET:
Kartik2112 Credit Card Transactions Fraud Detection (Kaggle)
- 1,296,675 train + 555,719 test redova
- Fraud rate: 0.58 % (train), 0.39 % (test)
- 20 originalnih + 9 inženjerski izvedenih feature-a
- Period: 1 Jan 2019 - 31 Dec 2020

METODOLOGIJA:
4 resampling tehnike (None, RandomOverSampler, SMOTE, SMOTE+Tomek)
   x
2 ensemble modela (Random Forest, XGBoost)
   =
8 konfiguracija, ocijenjeno na 6 imbalance-aware metrika.

DATOTEKE:
- workflow_diagram.png  ... obavezni dijagram metodologije
- workflow_diagram.py   ... reproducibilni skript koji generise dijagram
- eda_stats.json        ... statistika dataseta
