import pandas as pd
def describir_datos_rachas(data_frame_limpio):
    print("* DESCRIPCION DEL DATASET *")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo: {data_frame_limpio.dtypes}")

    #Estadisticas (SOLO APLICA PARA DATOS NUMERICOS)
    print("* ESTADISTICAS *")
    print(f"{data_frame_limpio[['id', 'user_id', 'current_streak', 'longest_streak']].describe()}")

    #Informacion de conteos valiosos
    print("* CONTEOS *")
    print(f"{data_frame_limpio['user_id'].value_counts()}")
    print(f"{data_frame_limpio['current_streak'].value_counts()}")
    print(f"{data_frame_limpio['longest_streak'].value_counts()}")

    #Describiendo las fechas
    print("* DESCRIPCION DE FECHAS *")
    print(f"{data_frame_limpio['created_at'].min()}")
    print(f"{data_frame_limpio['updated_at'].min()}")