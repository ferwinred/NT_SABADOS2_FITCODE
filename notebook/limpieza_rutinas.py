import pandas as pd

def limpiar_datos_rutinas(data_frame_sucio):
    
    data_frame_limpio = data_frame_sucio.copy()
    
    #1. Limpiar las columnas String del DF
    columnas_text = ["title", "difficulty"]
    for col in columnas_text:
        data_frame_limpio[col] = data_frame_limpio[col].astype("string").str.strip()
    
        #1.1 definir valores de string esperados
        valores_validos_title=["Entrenamiento de fuerza", "Yoga para principiantes", "Cardio intenso", "Entrenamiento funcional", "Baile fitness"]
        data_frame_limpio["title"]=data_frame_limpio["title"].where(
                data_frame_limpio["title"].isin(valores_validos_title),
                pd.NA
          )
        
        valores_validos_difficulty=["intermediate", "beginner", "advanced"]
        data_frame_limpio["difficulty"]=data_frame_limpio["difficulty"].where(
                data_frame_limpio["difficulty"].isin(valores_validos_difficulty),
                pd.NA
        )

        #2. limpiar las columnas numéricas del DF
        data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
        data_frame_limpio["durationMinutes"]=pd.to_numeric(data_frame_limpio["durationMinutes"])
        data_frame_limpio["authorUserId"]=pd.to_numeric(data_frame_limpio["authorUserId"])
        data_frame_limpio["isPublic"]=pd.to_numeric(data_frame_limpio["isPublic"])
    
        #2.1 limpiando campos numeros que no tengan valores validos 
        data_frame_limpio=data_frame_limpio[data_frame_limpio["durationMinutes"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["authorUserId"]>0]
        data_frame_limpio=data_frame_limpio[data_frame_limpio["isPublic"].isin([0,1])]
     
        #3. organizar las columnas de tipo fecha  
        data_frame_limpio["createdAt"]=pd.to_datetime(data_frame_limpio["createdAt"])

        #3.1 si una fecha no viene la reemplazamos por un valor por defecto 
        fecha_default=pd.to_datetime("2023-01-01")
        data_frame_limpio["createdAt"]=data_frame_limpio["createdAt"].fillna(fecha_default)

        #4. eliminar registros que tengan datos obligatorios vacios
        columnas_obligatorias=["id","durationMinutes","title","difficulty", "authorUserId", "isPublic"]
        data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

        #5. eliminar registros duplicados
        data_frame_limpio=data_frame_limpio.drop_duplicates()
    
    
    
    return data_frame_limpio