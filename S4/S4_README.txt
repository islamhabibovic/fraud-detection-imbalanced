S4 - Eksperimenti I (baseline + ablation)

ZADATAK:  Baseline modeli (Random Forest, ...), pocetak ablation study.
ISPORUKA: Tabela baseline rezultata.

BASELINE (bez resampling-a):
+-------------------+-----------+--------+-------+---------+--------+-------+
| Model             | Precision | Recall |   F1  | AUC-ROC | AUC-PR |  MCC  |
+-------------------+-----------+--------+-------+---------+--------+-------+
| Random Forest     |   0.962   |  0.751 | 0.843 |  0.951  |  0.838 | 0.851 |
| XGBoost           |   0.943   |  0.776 | 0.852 |  0.969  |  0.857 | 0.856 |
+-------------------+-----------+--------+-------+---------+--------+-------+

KOMENTAR:
Baseline ima visoku precision ali Recall < 0.78 - propusta puno fraud-a.
Ablation: bez feature engineering F1 pada za ~0.05; bez balansiranja Recall
pada za ~0.10. Time je opravdan dolazak na S5 (full eksperimenti).

KOMPLETNA TABELA SVIH 8 KONFIGURACIJA: results_table.csv
