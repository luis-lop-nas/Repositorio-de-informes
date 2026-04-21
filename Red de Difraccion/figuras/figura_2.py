import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'figure.figsize': (7, 5),
    'axes.grid': True,
    'grid.alpha': 0.3
})

m = np.array([1, 2, 3], dtype=float)
lambda_nm = np.array([590.28, 589.67, 590.94], dtype=float)
dlambda_nm = np.array([2.02, 0.96, 0.58], dtype=float)

w = 1.0 / dlambda_nm**2
lambda_mean = np.sum(w * lambda_nm) / np.sum(w)
dlambda_mean = np.sqrt(1.0 / np.sum(w))

fig, ax = plt.subplots()
ax.errorbar(
    m, lambda_nm, yerr=dlambda_nm, fmt='o', color='black',
    capsize=4, markersize=6, label='Valores experimentales por orden'
)
ax.axhline(
    lambda_mean, color='tab:red', linewidth=1.8,
    label=f'Media ponderada = {lambda_mean:.2f} ± {dlambda_mean:.2f} nm'
)
ax.axhline(589.3, color='tab:blue', linestyle='--', linewidth=1.4, label='Valor nominal sodio: 589,3 nm')

ax.set_xlabel('Orden de difracción |m|')
ax.set_ylabel('Longitud de onda λ (nm)')
ax.set_title('Longitud de onda de la lámpara de sodio')
ax.set_xticks([1, 2, 3])
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('figuras/figura_2.pdf', dpi=150, bbox_inches='tight')
