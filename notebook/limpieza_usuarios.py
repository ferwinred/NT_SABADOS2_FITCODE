import pandas as pd

def limpiar_datos_usuarios(data_frame_sucio):
     
    data_frame_sucio=data_frame_sucio.copy()

    #1. limpiar las columnas String del DF
    columnas_texto=["sex"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip(),str.lower()

        #1.1 definir valores de string esperados
        valores_validos_sex=["masculino","femenino"]
        data_frame_limpio["sex"]=data_frame_limpio["sex"].where(
                data_frame_limpio["sex"].isin(valores_validos_sex),
                pd.NA
          )
        
        #2. limpiar las columnas numéricas del DF
        data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
        data_frame_limpio["costo"]=pd.to_numeric(data_frame_limpio["costo"])

        #2.1 limpiando campos numeros que no tengan valores validos 
        data_frame_limpio=data_frame_limpio[data_frame_limpio["id"](0, 200)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["height_cm"](0, 250)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["weight_kg"](0, 200)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["date_of_birth"](0, 365 * 30)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["created_at"](0, 365 * 30)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["updated_at"](0, 365 * 30)]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["deleted_at"](0, 365 * 30)]

        #3. organizar las columnas de tipo fecha  
        data_frame_limpio["date_of_birth"]=pd.to_datetime(data_frame_limpio["date_of_birth"])
        data_frame_limpio["created_at"]=pd.to_datetime(data_frame_limpio["created_at"])
        data_frame_limpio["updated_at"]=pd.to_datetime(data_frame_limpio["updated_at"])
        data_frame_limpio["deleted_at"]=pd.to_datetime(data_frame_limpio["deleted_at"])

        #3.1 si una fecha no viene la reemplazamos por un valor por defecto 
        fecha_default=pd.to_datetime("2023-01-01")
        data_frame_limpio["date_of_birth"]=data_frame_limpio["date_of_birth"].fillna(0, 365 * 30)
        data_frame_limpio["created_at"]=data_frame_limpio["created_at"].fillna(0, 365 * 30)
        data_frame_limpio["updated_at"]=data_frame_limpio["updated_at"].fillna(0, 365 * 30)
        data_frame_limpio["deleted_at"]=data_frame_limpio["deleted_at"].fillna(0, 365 * 30)

        #4. eliminar registros que tengan datos obligatorios vacios
        columnas_obligatorias=["sex","full_name","email","password_hash"]
        data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

        #5. eliminar registros duplicados
        data_frame_limpio=data_frame_limpio.drop_duplicates()

    
    return data_frame_limpio
     