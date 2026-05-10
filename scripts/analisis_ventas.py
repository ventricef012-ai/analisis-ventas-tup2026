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

# Grafico de ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total_venta"].sum()

ventas_por_mes.plot(kind="bar", figsize=(12, 5), color="steelblue")
plt.title("Ventas Mensuales 2024")
plt.xlabel("Mes")
plt.ylabel("Total ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../resultados/grafico_ventas.png")
plt.show()

print("Listo!")
