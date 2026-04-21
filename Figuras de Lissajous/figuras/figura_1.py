import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'figure.figsize': (7, 5),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# Rellenar con datos experimentales reales
f_nom = np.array([50, 100, 200, 800, 3000], dtype=float)
f_rej = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)
df_rej = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)
f_cur = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)
df_cur = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)
f_auto = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)
df_auto = np.array([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=float)

fig, ax = plt.subplots()

if np.isfinite(f_rej).any():
    ax.errorbar(f_nom, f_rej, yerr=df_rej, fmt='o', capsize=4, label='Rejilla')
if np.isfinite(f_cur).any():
    ax.errorbar(f_nom, f_cur, yerr=df_cur, fmt='s', capsize=4, label='Cursores')
if np.isfinite(f_auto).any():
    ax.errorbar(f_nom, f_auto, yerr=df_auto, fmt='^', capsize=4, label='Automática')

ax.plot(f_nom, f_nom, 'k--', linewidth=1.2, label='f medida = f nominal')
ax.set_xlabel('Frecuencia nominal (Hz)')
ax.set_ylabel('Frecuencia medida (Hz)')
ax.set_title('Comparación de métodos de medida de frecuencia')
ax.legend(fontsize=10)

if not (np.isfinite(f_rej).any() or np.isfinite(f_cur).any() or np.isfinite(f_auto).any()):
    ax.text(0.5, 0.5, 'Rellenar arrays con datos\nexperimentales reales',
            transform=ax.transAxes, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('figuras/figura_1.pdf', dpi=150, bbox_inches='tight')
