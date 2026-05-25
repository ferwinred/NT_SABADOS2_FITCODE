import pandas as pd
def describir_datos_rutinas(data_frame_limpio):
    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo: {data_frame_limpio.dtypes}")


    #Estadisticas (SOLO APLICA PARA DATOS NUMERICOS)
    print("*** ESTADISTICAS ***")
    print(f"{data_frame_limpio[['id','difficulty','authorUserId','durationMinutes']].describe()}")

    #Informacion de conteos valiosos
    print("*** CONTEOS ***")
    print(f"{data_frame_limpio['difficulty'].value_counts()}")
    print(f"{data_frame_limpio['authorUserId'].value_counts()}")
    print(f"{data_frame_limpio['durationMinutes'].value_counts()}")


    #Describiendo las fechas
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"{data_frame_limpio['createdAt'].max()}")
    print(f"{data_frame_limpio['updatedAt'].max()}")