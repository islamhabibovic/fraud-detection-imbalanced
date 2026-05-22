"""
Generates a publication-quality workflow diagram (PNG) for the methodology
section. MANDATORY per assignment rubric ("Methodology bez dijagrama toka -
desk reject zastavica").
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FIG = Path(__file__).parent / "results" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13); ax.set_ylim(0, 11); ax.axis("off")

def box(x, y, w, h, text, color, ax, textcolor="black", fontsize=10, fontweight="bold"):
    b = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.08,rounding_size=0.15",
                       linewidth=1.6, edgecolor="black", facecolor=color)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=fontweight, color=textcolor)

def arrow(x1,y1,x2,y2, ax, color="#2c3e50"):
    a = FancyArrowPatch((x1,y1),(x2,y2), arrowstyle="-|>", mutation_scale=18,
                        color=color, linewidth=1.6)
    ax.add_patch(a)

# ---------- Stage 1 : data acquisition --------------------------------------
box(3.5, 9.7, 6, 0.9,
    "Credit Card Fraud Dataset (Kartik2112, Kaggle)\n"
    "1,296,675 train  -  555,719 test  -  ~0.5% fraud rate",
    "#dfe6e9", ax, fontsize=10)

arrow(6.5, 9.7, 6.5, 9.1, ax)

# ---------- Stage 2 : EDA & preprocessing ----------------------------------
box(0.3, 7.9, 4, 1.1, "EDA & Feature Engineering\n- temporal (hour, day, age)\n- haversine distance",
    "#a3d5ff", ax, fontsize=9)
box(4.8, 7.9, 3.4, 1.1, "Preprocessing\n- LabelEncoder (cat. cols)\n- StandardScaler (num. cols)",
    "#a3d5ff", ax, fontsize=9)
box(8.7, 7.9, 4, 1.1, "Train / Test split\n- predefined (Kartik2112)\n- fraud rate preserved",
    "#a3d5ff", ax, fontsize=9)

arrow(2.3, 7.9, 2.3, 7.0, ax)
arrow(6.5, 7.9, 6.5, 7.0, ax)
arrow(10.7, 7.9, 10.7, 7.0, ax)

# ---------- Stage 3 : resampling --------------------------------------------
box(0.0, 5.5, 13, 1.4,
    "Resampling techniques applied only on the TRAINING set",
    "#fff3c4", ax, fontsize=11)

box(0.3, 5.6, 3, 0.7, "None (baseline)", "#fdcb6e", ax, fontsize=9)
box(3.6, 5.6, 3, 0.7, "Random OverSampler", "#fdcb6e", ax, fontsize=9)
box(6.9, 5.6, 3, 0.7, "SMOTE",              "#fdcb6e", ax, fontsize=9)
box(10.2, 5.6, 2.6, 0.7,"SMOTE + Tomek",     "#fdcb6e", ax, fontsize=9)

arrow(1.8, 5.6, 1.8, 4.8, ax)
arrow(5.1, 5.6, 5.1, 4.8, ax)
arrow(8.4, 5.6, 8.4, 4.8, ax)
arrow(11.5, 5.6, 11.5, 4.8, ax)

# ---------- Stage 4 : training models ---------------------------------------
box(0.3, 3.6, 6, 1.1, "Random Forest\n200 trees, depth=12",
    "#b8f0c5", ax, fontsize=10)
box(6.7, 3.6, 6, 1.1, "XGBoost\n300 trees, depth=6, lr=0.1",
    "#b8f0c5", ax, fontsize=10)

arrow(3.3, 3.6, 3.3, 2.9, ax)
arrow(9.7, 3.6, 9.7, 2.9, ax)

# ---------- Stage 5 : evaluation --------------------------------------------
box(0.3, 1.7, 12.4, 1.1,
    "Evaluation on test set\nPrecision  -  Recall  -  F1  -  AUC-ROC  -  AUC-PR  -  MCC  -  Confusion Matrix",
    "#fab1a0", ax, fontsize=10)

arrow(6.5, 1.7, 6.5, 1.0, ax)

# ---------- Stage 6 : comparative analysis ---------------------------------
box(2.5, 0.0, 8, 0.9,
    "Comparative analysis  -  statistical significance (Friedman + Nemenyi)  -  best configuration",
    "#dda0dd", ax, fontsize=10)

# ---------- title -----------------------------------------------------------
ax.set_title("Methodology Workflow Diagram",
             fontsize=15, fontweight="bold", pad=10)

plt.tight_layout()
plt.savefig(FIG / "workflow_diagram.png", dpi=170, bbox_inches="tight",
            facecolor="white")
plt.close()
print("[OK] workflow_diagram.png saved")
