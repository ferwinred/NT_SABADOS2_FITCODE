import pandas as pd
from notebook.limpieza_rutinas import limpiar_datos_rutinas
from notebook.consumo_rutinas import consumo_rutinas
from notebook.transformar_rutinas  import transformar_rutinas
from notebook.graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

rutinas = consumo_rutinas()
rutinas_ordenadas = pd.DataFrame(rutinas)
limpiar_datos_rutinas(rutinas_ordenadas)
agrupaciones = transformar_rutinas(rutinas_ordenadas)
print(agrupaciones["agrupacion1"])
graficar_barras(
    agrupaciones["agrupacion1"],
    "difficulty",
    "Duracion_total",
    "Grafico de duracion total por dificultad", 
    "#FF5722",
    "duracion_por_dificultad.png"
)

