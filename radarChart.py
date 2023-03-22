# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

# Definir los valores de las categorías en un DataFrame de pandas
data = pd.DataFrame({
    'Gestión de la Organización': [87],
    '                      Gerencia de Trabajo': [96],
    '                            Gerencia de Materiales': [82],
    'Gerencia de Información': [79],
    'Soporte Gerencial                     ': [100],
    'Gerencia de Ingeniería                          ': [85]
})

# Reordenar las columnas del DataFrame para que coincidan con el orden en que se mostrarán en el gráfico
data = data[['Gestión de la Organización',
             '                      Gerencia de Trabajo',
             '                            Gerencia de Materiales',
             'Gerencia de Información',
             'Soporte Gerencial                     ',
             'Gerencia de Ingeniería                          ']]



# Obtener el número de categorías y crear los ángulos correspondientes para el gráfico de radar
categories = list(data)
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Inicializar el gráfico de radar como un subplot polar
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Definir los valores de los márgenes y espacios entre subplots
top = 0.770
bottom = 0.230
left = 0.11
right = 0.89
hspace = 0.2
wspace = 0.2

# Aplicar los ajustes a los subplots
fig.subplots_adjust(top=top, bottom=bottom, left=left, right=right, hspace=hspace, wspace=wspace)

# Ajustar la dirección del ángulo cero y el sentido de giro
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Dibujar los ejes del gráfico de radar
plt.xticks(angles[:-1], categories, color='grey', size=12)

# Añadir las etiquetas del eje radial
ax.set_rlabel_position(0)
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90",
                                                          "100"], color="grey", size=6)
plt.ylim(0, 100)

# Trazar las líneas para cada categoría y rellenar el área debajo de ellas
for i, row in data.iterrows():
    values = row.values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=3, linestyle='solid', label=row.name)
    ax.fill(angles, values, facecolor='blue', alpha=0.2)


# Ajustar la separación entre las etiquetas del eje x
ax.tick_params(axis='x', labelsize=10, pad=6)


# Definir los valores de las categorías en el DataFrame de pandas de nuevo (solo para mostrar la lista de categorías)
data = pd.DataFrame({
    'Gestión de la Organización': [87],
    'Gerencia de Trabajo': [96],
    'Gerencia de Materiales': [82],
    'Gerencia de Información': [79],
    'Soporte Gerencial': [100],
    'Gerencia de Ingeniería': [85]
})

# Define number of variables
categories = list(data)
# Add category list box
x_pos = 1.05  # X position of text box
y_pos = 1.125  # Y position of text box
width = 0.25  # Width of text box
height = 0.25  # Height of text box
spacing = 0.015  # Spacing between lines

# Crear una lista de strings con los nombres de las categorías y sus valores numéricos

cat_vals = [f"{category} {value:}%" for category, value in zip(categories, data.values.flatten().tolist())]

# Crear una cadena de texto con las categorías y sus valores numéricos
cat_text = '\n'.join(cat_vals)

text_box = plt.text(x_pos, y_pos, 'Evaluacion de Categorías:\n\n' + cat_text, fontsize=7,
                    bbox=dict(facecolor='white',
                              edgecolor='black',
                              pad=0.8,
                              boxstyle='round',
                              linewidth=0.8),
                    transform=ax.transAxes,
                    va='top',
                    ha='left',
                    zorder=10,
                    clip_on=False)

plt.title('E&M Solutions C.A.', size=20, pad=30)
plt.show()
