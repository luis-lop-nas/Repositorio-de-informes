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

# Datos experimentales: torsion de la fibra
n = np.array([0, 1, 2, 3, 4, 5], dtype=float)
V = np.array([2.62, 1.83, 1.58, 1.43, 0.93, 0.80], dtype=float)
dV = 0.005  # V, tipo B (resolucion/2 para lecturas con dos decimales)

V0 = V[0]
A = 10.0 * np.log10(V / V0)
dA = (10.0 / np.log(10.0)) * np.sqrt((dV / V) ** 2 + (dV / V0) ** 2)

# Ajuste lineal A = m*n + b
coef, cov = np.polyfit(n, A, 1, cov=True)
m, b = coef
m_err, b_err = np.sqrt(np.diag(cov))

x_fit = np.linspace(n.min(), n.max(), 200)
y_fit = m * x_fit + b

fig, ax = plt.subplots()
ax.errorbar(
    n,
    A,
    yerr=dA,
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
    label=rf"A = ({m:.3f}±{m_err:.3f})N + ({b:.3f}±{b_err:.3f})",
)
ax.set_xlabel("Número de vueltas N")
ax.set_ylabel("Atenuación A (dB)")
ax.set_title("Atenuación por torsión de la fibra")
ax.legend(fontsize=9)

plt.tight_layout()
out = Path(__file__).resolve().parent / "figura_1.pdf"
plt.savefig(out, dpi=150, bbox_inches="tight")
