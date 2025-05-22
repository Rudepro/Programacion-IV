import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo dirigido
G = nx.DiGraph()

# Aristas del árbol ((6 - 2) + (5 ^ 2))
edges = [
    ('+', '-'),
    ('+', '^'),
    ('-', '6'),
    ('-', '2a'),
    ('^', '5'),
    ('^', '2b')
]
G.add_edges_from(edges)

# Posiciones jerárquicas
pos = {
    '+': (0, 3),       # Raíz - Nivel 0
    '-': (-2, 2),      # Nivel 1
    '^': (2, 2),       # Nivel 1
    '6': (-3, 1),      # Nivel 2 - Hoja
    '2a': (-1, 1),     # Nivel 2 - Hoja
    '5': (1, 1),       # Nivel 2 - Hoja
    '2b': (3, 1)       # Nivel 2 - Hoja
}

# Dibujar
fig, ax = plt.subplots(figsize=(10, 6))
nx.draw(
    G, pos, ax=ax,
    with_labels=True,
    node_color='lightgreen',
    node_size=2000,
    font_size=14,
    font_weight='bold',
    arrows=True
)

# Añadir anotaciones de niveles
plt.text(0, 3.2, "Raíz (Nivel 0)", fontsize=10, ha='center', color='darkblue')
plt.text(-2, 2.2, "Nivel 1\n(Padre)", fontsize=9, ha='center', color='darkred')
plt.text(2, 2.2, "Nivel 1\n(Padre)", fontsize=9, ha='center', color='darkred')
plt.text(-3, 0.8, "Hoja\n(Nodo hijo)", fontsize=9, ha='center', color='purple')
plt.text(-1, 0.8, "Hoja\n(Nodo hijo)", fontsize=9, ha='center', color='purple')
plt.text(1, 0.8, "Hoja\n(Nodo hijo)", fontsize=9, ha='center', color='purple')
plt.text(3, 0.8, "Hoja\n(Nodo hijo)", fontsize=9, ha='center', color='purple')

# Añadir título y leyenda
ax.set_title("Árbol de expresión: ((6 - 2) + (5 ^ 2))", fontsize=16, fontweight='bold')
ax.axis('off')

# Crear leyenda manual
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='lightblue', label='Nodo'),
    Patch(facecolor='none', edgecolor='black', label='Flecha: relación padre-hijo')
]
plt.legend(handles=legend_elements, loc='lower right')

plt.show()
