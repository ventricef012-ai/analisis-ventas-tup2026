import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("../datos/ventas.csv")

# Calcular total de venta por fila
df["total_venta"] = df["cantidad"] * df["precio_unitario"]

# Indicadores basicos
ventas_totales = df["total_venta"].sum()
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto mas vendido:", producto_mas_vendido)

# Grafico simple
df["total_venta"].plot()
plt.title("Ventas")
plt.savefig("../resultados/grafico_ventas.png")
plt.show()

print("Listo!")