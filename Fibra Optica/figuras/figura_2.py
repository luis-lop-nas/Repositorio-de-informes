import os
import tempfile
import numpy as np
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(tempfile.gettempdir()) / "xdg_cache"))

import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "figure.figsize": (7, 5),
    "axes.grid": True,
    "grid.alpha": 0.3,
})

# Datos experimentales: separacion entre terminales
l = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
V = np.array([30.7, 26.7, 24.4, 20.4, 18.0, 15.9, 14.5, 13.2, 12.1, 11.4], dtype=float)
dV = 0.05  # tipo B (resolucion/2 para lecturas con una decimal)
V_ref = V[0]
dV_ref = dV

# Ajuste exponencial directo: ln(V)=k*l+b
coef_ln, cov_ln = np.polyfit(l, np.log(V), 1, cov=True)
k, b_ln = coef_ln
k_err, b_ln_err = np.sqrt(np.diag(cov_ln))

# Atenuacion relativa usando referencia medida en l=1 mm (sin extrapolar l=0)
A_rel = 10.0 * np.log10(V / V_ref)
dA_rel = (10.0 / np.log(10.0)) * np.sqrt((dV / V) ** 2 + (dV_ref / V_ref) ** 2)

# Ajuste lineal A_rel = m*l + b
coef_A, cov_A = np.polyfit(l, A_rel, 1, cov=True)
m, b = coef_A
m_err, b_err = np.sqrt(np.diag(cov_A))

x_fit = np.linspace(l.min(), l.max(), 300)
y_fit = m * x_fit + b

fig, ax = plt.subplots()
ax.errorbar(
    l,
    A_rel,
    yerr=dA_rel,
    fmt="o",
    color="black",
    capsize=4,
    markersize=5,
    label="Datos experimentales",
)
ax.plot(
    x_fit,
    y_fit,
    "r-",
    linewidth=1.5,
    label=rf"A_rel = ({m:.3f}±{m_err:.3f})l + ({b:.3f}±{b_err:.3f})",
)
ax.set_xlabel("Separación l (mm)")
ax.set_ylabel("Atenuación relativa A_rel (dB)")
ax.set_title("Atenuación relativa por separación entre terminales")
ax.legend(fontsize=9)

plt.tight_layout()
out = Path(__file__).resolve().parent / "figura_2.pdf"
plt.savefig(out, dpi=150, bbox_inches="tight")
