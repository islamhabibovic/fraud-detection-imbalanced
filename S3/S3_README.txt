S3 - Preprocessing

ZADATAK:  Ciscenje, normalizacija, feature engineering, EDA s vizualizacijama.
ISPORUKA: Jupyter notebook - preprocessing + EDA.

PIPELINE (fraud_detection_experiment.py):
1. Load Kartik2112 dataset (predefinisani train/test split).
2. Feature engineering:
   - temporal: hour, day-of-week, age (iz dob)
   - spatial:  haversine distance kupac-trgovac
   - +9 dodatnih feature-a
3. Encoding:  LabelEncoder za kategoricke (category, merchant, job, gender)
4. Scaling:   StandardScaler za numericke
5. Missing values: 0 (dataset cist)

EDA:
- Class distribution u logaritamskoj skali i u procentima
  (figures/class_distribution.png)
- Provjereno da resampling se aplicira SAMO na trening setu - test set
  zadrzava originalnu 0.39 % stopu fraud-a.
