import pandas as pd

def limpiar_datos_rutinas(data_frame_sucio):
    
    data_frame_limpio = data_frame_sucio.copy()
    
    #1. Limpiar las columnas String del DF
    columnas_text = ["tittle", "difficulty"]
    for col in columnas_text:
        data_frame_limpio[col] = data_frame_limpio[col].astype("string").str.strip()
    
        #1.1 definir valores de string esperados
        valores_validos_tittle=["Entrenamiento de fuerza", "Yoga para principiantes", "Cardio intenso", "Entrenamiento funcional", "Baile fitness"]
        data_frame_limpio["tittle"]=data_frame_limpio["tittle"].where(
                data_frame_limpio["tittle"].isin(valores_validos_tittle),
                pd.NA
          )
        
        valores_validos_difficulty=["fácil", "intermedio", "avanzado"]
        data_frame_limpio["difficulty"]=data_frame_limpio["difficulty"].where(
                data_frame_limpio["difficulty"].isin(valores_validos_difficulty),
                pd.NA
        )

        #2. limpiar las columnas numéricas del DF
        data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
        data_frame_limpio["duration_minutes"]=pd.to_numeric(data_frame_limpio["duration_minutes"])
        data_frame_limpio["author_user_id"]=pd.to_numeric(data_frame_limpio["author_user_id"])
        data_frame_limpio["is_public"]=pd.to_numeric(data_frame_limpio["is_public"])
    
        #2.1 limpiando campos numeros que no tengan valores validos 
        data_frame_limpio=data_frame_limpio[data_frame_limpio["duration_minutes"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["author_user_id"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["is_public"].isin([0,1])]
     
        #3. organizar las columnas de tipo fecha  
        data_frame_limpio["created_at"]=pd.to_datetime(data_frame_limpio["created_at"])

        #3.1 si una fecha no viene la reemplazamos por un valor por defecto 
        fecha_default=pd.to_datetime("2023-01-01")
        data_frame_limpio["created_at"]=data_frame_limpio["created_at"].fillna(fecha_default)

        #4. eliminar registros que tengan datos obligatorios vacios
        columnas_obligatorias=["id","duration_minutes","tittle","difficulty", "author_user_id", "is_public"]
        data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

        #5. eliminar registros duplicados
        data_frame_limpio=data_frame_limpio.drop_duplicates()
    
    
    
    return data_frame_limpio