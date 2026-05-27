S5 - Eksperimenti II (full + hyperparameter tuning)

ZADATAK:  Glavni modeli, hyperparameter tuning, usporedba s baselineom.
ISPORUKA: Finalni eksperimenti + sve metrike (F1, AUC, RMSE...).

SVI EKSPERIMENTI - 8 KONFIGURACIJA, 6 METRIKA (results_table.csv).

NAJBOLJA KONFIGURACIJA: SMOTE+Tomek + XGBoost
   F1       = 0.873
   Recall   = 0.867   (vs 0.751 baseline RF  =>  + 11.6 pp)
   AUC-PR   = 0.879
   MCC      = 0.874

STATISTICKA VALIDACIJA:
   Friedman test + Nemenyi post-hoc, p < 0.01
   SMOTE+Tomek znacajno bolji od baseline-a.

FIGURE (folder figures/):
   metrics_comparison.png    - svih 6 metrika u 2x3 grid
   roc_curves.png            - ROC krive za 8 konfiguracija
   pr_curves.png             - Precision-Recall krive
   confusion_matrix_best.png - CM najboljeg modela
   feature_importance.png    - top-20 feature-a (XGBoost gain)
