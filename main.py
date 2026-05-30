import pandas as pd
from notebook.limpieza_rutinas import limpiar_datos_rutinas
from notebook.consumo_rutinas import consumo_rutinas
from notebook.transformar_rutinas  import transformar_rutinas
from notebook.consumo_usuarios import consumo_usuarios
from notebook.limpieza_usuarios import limpiar_datos_usuarios
from notebook.transformar_usuarios import transformar_usuarios
from notebook.graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

rutinas = consumo_rutinas()
rutinas_ordenadas = pd.DataFrame(rutinas)
limpiar_datos_rutinas(rutinas_ordenadas)
agrupaciones = transformar_rutinas(rutinas_ordenadas)

graficar_barras(
    agrupaciones["agrupacion1"],
    "difficulty",
    "Duracion_total",
    "Grafico de duracion total por dificultad", 
    ["#FF5722", "#2196F3", "#4CAF50"],
    "duracion_por_dificultad.png"
)

graficar_lineas(
    agrupaciones["agrupacion2"],
    "id",
    "duracion_promedio",
    "Grafico de duracion promedio de ejercicios", 
    "#FF5722",
    "duracion_promedio_lineas.png"
)


usuarios = consumo_usuarios()
data_frame_usuarios = pd.DataFrame(usuarios)
data_frame_usuarios_limpio = limpiar_datos_usuarios(data_frame_usuarios)
agrupaciones=transformar_usuarios(data_frame_usuarios_limpio)

graficar_torta(
    agrupaciones["agrupacion1"],
    "sex",
    "conteo_por_sexo",
    "Cantidad de usuarios por sexo",
     ["#FF5722", "#2196F3"],
    "usuarios_por_sexo.png"
)
