import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'figure.figsize': (7, 5),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# Figura de referencia teorica (ejemplo 2:3)
t = np.linspace(0, 2*np.pi, 2000)
ratio_x = 2
ratio_y = 3
phi = np.pi/2

x = np.sin(ratio_x * t)
y = np.sin(ratio_y * t + phi)

fig, ax = plt.subplots()
ax.plot(x, y, color='black', linewidth=1.2)
ax.set_xlabel('Canal X (u.a.)')
ax.set_ylabel('Canal Y (u.a.)')
ax.set_title('Lissajous teórica de referencia (2:3)')
ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig('figuras/figura_2.pdf', dpi=150, bbox_inches='tight')
