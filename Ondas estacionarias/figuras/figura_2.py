"""
figura_2.py  –  Perfiles espaciales de los seis primeros modos normales
                de una cuerda de longitud L con extremos fijos.

Genera: ../imagenes/modos_normales.pdf
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10})

x = np.linspace(0, 1, 500)   # longitud normalizada x/L

fig, axes = plt.subplots(6, 1, figsize=(5.5, 5.5), sharex=True)
fig.subplots_adjust(hspace=0.08)

colores = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']

for i, (ax, color) in enumerate(zip(axes, colores), start=1):
    y = np.sin(i * np.pi * x)
    ax.plot(x, y, color=color, linewidth=1.6)
    ax.plot(x, -y, color=color, linewidth=1.6, linestyle='--', alpha=0.45)
    ax.axhline(0, color='gray', linewidth=0.6)
    ax.set_ylim(-1.4, 1.4)
    ax.set_yticks([])
    ax.set_ylabel(f'$n={i}$', rotation=0, labelpad=28, va='center', fontsize=10)
    # marcar nodos
    nodos = np.linspace(0, 1, i + 1)
    ax.plot(nodos, np.zeros_like(nodos), 'ko', markersize=3, zorder=5)
    ax.spines[['top', 'right', 'left']].set_visible(False)

axes[-1].set_xlabel('$x/L$')
axes[-1].set_xticks([0, 0.25, 0.5, 0.75, 1.0])
axes[-1].set_xticklabels(['0', '', '$L/2$', '', '$L$'])

fig.suptitle('Primeros seis modos normales de una cuerda fija en sus extremos',
             fontsize=10, y=1.01)

plt.tight_layout()
plt.savefig('../imagenes/modos_normales.pdf', dpi=300, bbox_inches='tight')
plt.savefig('../imagenes/modos_normales.png', dpi=300, bbox_inches='tight')
print("Figura guardada en ../imagenes/modos_normales.{pdf,png}")
