from notebook.consumo_usuarios import consumo_usuarios
from notebook.limpieza_usuarios import limpiar_datos_usuarios
from notebook.transformar_usuarios import transformar_usuarios
from notebook.graficacion_usuarios import graficar_barras

import pandas as pd

usuarios = consumo_usuarios()

data_frame_usuarios = pd.DataFrame(
    usuarios
)

data_frame_usuarios_limpio = limpiar_datos_usuarios(
    data_frame_usuarios
)

agrupaciones=transformar_usuarios(
    data_frame_usuarios_limpio
)

graficar_barras(
    agrupaciones["agrupacion1"],
    columna_categorias="sex",
    columna_valores="conteo_por_sexo",
    titulo="Cantidad de usuarios por sexo",
    color_barras="#FF5733",
    nombre_archivo="usuarios_por_sexo.png"
)