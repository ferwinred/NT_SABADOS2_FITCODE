import random

from datetime import datetime,timedelta

def generar_rachas(numeroSimulaciones):

    nombres=["chispa","magma","flama", "rayo","tormenta"]
    fechaInicio=datetime(2026,1,2)
    created_at=datetime(2026,4,11)
    updated_at=datetime(2026,4,11)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.randint(0,200),
            "user_id":random.randint(0,200),
            "name":random.choice(nombres),
            "current_streak":random.randint(0,30),
            "last_date":fechaInicio+timedelta(days=random.randint(0,60)),
            "longest_streak":random.randint(0,30),
            "created_at ":created_at +timedelta(days=random.randint(0,60)),
            "updated_at ":updated_at +timedelta(days=random.randint(0,60)),
        }

        simulaciones.append(simulacion)
    return simulaciones