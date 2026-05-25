import pandas as pd

def transformar_rutinas(data_frame_limpio):
    
    filtro1 = data_frame_limpio.query("isPublic == 1")
    agrupacion1 = filtro1.groupby("difficulty")["durationMinutes"].sum().reset_index(name="Duracion_total")

    filtro2 = data_frame_limpio.query("durationMinutes > 0")
    agrupacion2 = filtro2.groupby("id")["durationMinutes"].mean().reset_index(name="duracion_promedio")

    filtro3 = data_frame_limpio.query("authorUserId > 0")
    agrupacion3 = filtro3.groupby("authorUserId")["id"].count().reset_index(name="cantidad_rutinas")
    
    filtro4 = data_frame_limpio.query("isPublic == 1")
    agrupacion4 = filtro4.groupby("difficulty")["id"].count().reset_index(name="cantidad_rutinas")

    agrupacion_resumen={
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4
    }
    
    return agrupacion_resumen
