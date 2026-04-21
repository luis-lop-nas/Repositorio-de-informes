"""
figura_1.py  –  Frecuencia de resonancia frente al número de modo
                para las cuatro tensiones de trabajo.

Genera: ../imagenes/ajuste_frecuencias.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'figure.figsize': (6, 4.5),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# ── Datos experimentales ────────────────────────────────────────────────────
L   = 0.1315   # m
dL  = 0.0005   # m
df  = 0.5      # Hz

modos = np.array([3, 4, 5, 6, 7, 8])

frecuencias = {
    r"$T_0$": np.array([8.709, 11.709, 14.709, 17.109, 23.009, 25.009]),
    r"$T_1$": np.array([np.nan, 12.709, 16.409, 22.809, 26.409, 28.709]),
    r"$T_2$": np.array([12.509, 16.709, 22.609, 26.909, 31.309, 35.009]),
    r"$T_3$": np.array([14.509, 18.809, 24.309, 28.809, 33.909, 38.309]),
}

# Incertidumbre de frecuencia: δf = 0.5 Hz (resolución del generador / 2)
# Se representa como barra de error constante en y.
# Las barras en x no aplican (n es entero exacto).

colores   = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
marcadores = ["o", "s", "^", "D"]

fig, ax = plt.subplots()

for (etiqueta, f), color, marcador in zip(frecuencias.items(), colores, marcadores):
    mascara = ~np.isnan(f)
    n_ok = modos[mascara]
    f_ok = f[mascara]
    dy   = np.full(len(f_ok), df)   # δf = 0.5 Hz para todos los puntos

    # Ajuste lineal
    slope, intercept, r, p, se = linregress(n_ok, f_ok)

    # Puntos con barras de error
    ax.errorbar(n_ok, f_ok, yerr=dy, fmt=marcador, color=color,
                capsize=4, markersize=5, linewidth=0,
                elinewidth=1.2, label=etiqueta)

    # Recta de ajuste
    n_fit = np.linspace(2.5, 8.5, 200)
    ax.plot(n_fit, slope * n_fit + intercept, linestyle="--",
            color=color, linewidth=1.3, alpha=0.85)

ax.set_xlabel("Número de modo $n$")
ax.set_ylabel(r"$f_n$ (Hz)")
ax.set_title("Frecuencia de resonancia frente al modo")
ax.legend(fontsize=10, loc="upper left")
ax.set_xlim(2.5, 8.5)
ax.set_xticks(modos)

plt.tight_layout()
plt.savefig("../imagenes/ajuste_frecuencias.pdf", dpi=300, bbox_inches="tight")
plt.savefig("../imagenes/ajuste_frecuencias.png", dpi=300, bbox_inches="tight")
print("Figura guardada en ../imagenes/ajuste_frecuencias.{pdf,png}")
