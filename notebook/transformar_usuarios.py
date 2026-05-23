import pandas as pd

def transformar_usuarios(data_frame_limpio):

    print("Data frame limpio:")
    print(data_frame_limpio)
     # 1. Limpiar columnas string
    filtro1 = data_frame_limpio.query("sex=='M' or sex=='F'")
    agrupacion1 = filtro1.groupby("sex")["id"].count().reset_index(name="conteo_por_sexo")

    filtro2 = data_frame_limpio.query("weightKg > 0")
    agrupacion2 = filtro2.groupby("sex")["weightKg"].mean().reset_index(name="peso_promedio_por_sexo")

    filtro3 = data_frame_limpio.query("heightCm > 0")
    agrupacion3 = filtro3.groupby("sex")["heightCm"].mean().reset_index(name="altura_promedio_por_sexo")

    filtro4 = data_frame_limpio.query("role >= 0")
    agrupacion4 = filtro4.groupby("role")["id"].count().reset_index(name="cantidad_por_rol")

    filtro5 = data_frame_limpio.query("weightKg > 0")
    agrupacion5 = filtro5.groupby("role")["weightKg"].mean().reset_index(name="peso_promedio_por_rol")

    agrupacion_resumen={
         "agrupacion1": agrupacion1,
         "agrupacion2": agrupacion2,
         "agrupacion3": agrupacion3,
         "agrupacion4": agrupacion4,
         "agrupacion5": agrupacion5
     }
    
    return agrupacion_resumen
    