import pandas as pd              # importo pandas usado para los analisis de datos
import matplotlib.pyplot as plt   # importo matplotlib para el uso de graficos

df = pd.read_csv("CasosNuevosSinSintomas.csv")          # uso de pandas para leer estos csv
df2 = pd.read_csv("CasosNuevosSinSintomas_T.csv")

nombre_region = input("Región: ").capitalize()    # para todo lo que se ingrese la primera letra estara en mayusculas y lo demas en minusculas
                                                # se puede ingresar tanto como el indice o nombre de la region
if nombre_region.isdigit():
    nombre_region = int(nombre_region)

#para el uso de graficos uso los ejes X e Y en datos de una cantidad de 2 semanas segun lo ingresado

eje_x = []
eje_y = []

suma = 0
for region in df.iterrows():                        # iterar las filas
    nombre_region_iteracion = region[1][0]
    indice_region = region[0]+1
    if nombre_region == nombre_region_iteracion or nombre_region == indice_region:
        indice_region_seleccionada = indice_region
        nombre_region_seleccionada = nombre_region_iteracion
        i = 1
        dia = -14
        while dia <= -1:
            datos = region[1][dia]
            suma += datos
            eje_x.append(i)
            eje_y.append(suma)
            dia += 1
            i += 1

eje_x2 = []
eje_y2 = []

datos_ultimas_2_semanas = df2[(df2["Region"].index >= len(df2["Region"].index)-14)]
casos_region_seleccionada_ultimas_dos_semanas = datos_ultimas_2_semanas[nombre_region_seleccionada]

suma_columnas = []
i = 0
for region in df2.columns:
    if i != 0 and i != len(df2.columns)-1:
        columna = df2[region]
        sumatoria_columna = columna.sum()
        suma_columnas.append(sumatoria_columna)
    i += 1

print(suma_columnas)
                                    # ver la region con mas y menos contagios
max_contagios = suma_columnas[0]
min_contagios = suma_columnas[0]
i = 1
for valor in suma_columnas:
    if valor > max_contagios:
        max_contagios = valor
        i_max = i
    if valor < min_contagios:
        min_contagios = valor
        i_min = i

    i += 1

print(f"\nLa región con más contagios es la {i_max}° región con", max_contagios, "casos.")
print(f"La región con menos contagios es la {i_min}° región con", min_contagios, "casos.")

for dia in range(1, len(casos_region_seleccionada_ultimas_dos_semanas)+1):
    eje_x2.append(dia)

plt.style.use("ggplot")                                             #Esta parte de aca es todo para editar, insertar, poner titulos,crear graficos
plt.title("Casos de contagio las útlimas 2 semanas")
plt.plot(eje_x2, casos_region_seleccionada_ultimas_dos_semanas, label="No acumulativos")      # como los ejes X e Y, tambien para cambiar los estilos, colores
plt.plot(eje_x, eje_y, linewidth=1, color="b", label="Acumulativos")        #, ponerle nombres a los ejes x e y y entre otros mas.
plt.xlabel("Día")
plt.ylabel("Cantidad de contagios")
plt.xticks(eje_x)
plt.legend()
plt.tight_layout()
plt.show()                                       # para mostrar el grafico