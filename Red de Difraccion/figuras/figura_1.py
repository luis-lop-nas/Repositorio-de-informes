import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'figure.figsize': (7, 5),
    'axes.grid': True,
    'grid.alpha': 0.3
})

m1 = np.arange(1, 11)
dx1_mm = np.array([26, 52, 78, 104, 130, 156, 182, 208, 234, 260], dtype=float)
ddx1_mm = np.full_like(dx1_mm, 1.0)

m2 = np.arange(1, 15)
dx2_mm = np.array([18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252], dtype=float)
ddx2_mm = np.full_like(dx2_mm, 1.0)

slope1, intercept1, r1, _, _ = stats.linregress(m1, dx1_mm)
slope2, intercept2, r2, _, _ = stats.linregress(m2, dx2_mm)

m1_fit = np.linspace(m1.min(), m1.max(), 200)
m2_fit = np.linspace(m2.min(), m2.max(), 200)

dx1_fit = slope1 * m1_fit + intercept1
dx2_fit = slope2 * m2_fit + intercept2

fig, ax = plt.subplots()

ax.errorbar(
    m1, dx1_mm, yerr=ddx1_mm, fmt='o', color='black',
    capsize=4, markersize=5, label='Datos z = 0,200 m'
)
ax.plot(
    m1_fit, dx1_fit, color='black', linewidth=1.5,
    label=f'Ajuste z=0,200: Δx = ({slope1:.2f}) m + ({intercept1:.2f}), R²={r1**2:.4f}'
)

ax.errorbar(
    m2, dx2_mm, yerr=ddx2_mm, fmt='s', color='tab:blue',
    capsize=4, markersize=5, label='Datos z = 0,140 m'
)
ax.plot(
    m2_fit, dx2_fit, color='tab:blue', linewidth=1.5,
    label=f'Ajuste z=0,140: Δx = ({slope2:.2f}) m + ({intercept2:.2f}), R²={r2**2:.4f}'
)

ax.set_xlabel('Orden de difracción m')
ax.set_ylabel('Separación entre máximos simétricos Δx (mm)')
ax.set_title('Caracterización de la red: Δx frente a m')
ax.legend(fontsize=9, loc='upper left')

plt.tight_layout()
plt.savefig('figuras/figura_1.pdf', dpi=150, bbox_inches='tight')
