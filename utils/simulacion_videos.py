import random
from datetime import datetime, timedelta

def generar_simulacion(numeroSimulaciones):

    # Datos organizados correctamente (todo relacionado)
    videos = [
        {"tipo": "rutina cardio", "codigo": "vid001", "duracion": 19},
        {"tipo": "entrenamiento fuerza", "codigo": "vid002", "duracion": 30},
        {"tipo": "yoga", "codigo": "vid003", "duracion": 20}
    ]

    usuarios = ["user01", "user02", "user03", "user04"]
    fechaInicio = datetime(2026, 1, 2)

    simulaciones = []
    for _ in range(numeroSimulaciones):

        video = random.choice(videos)

        simulacion = {
            "id": random.randint(0, 200),
            "usuario": random.choice(usuarios),
            "tipo_video": video["tipo"],
            "codigo": video["codigo"],
            "duracion_min": video["duracion"],
            "calorias_quemadas": random.randint(50, 400),
            "fecha": fechaInicio + timedelta(days=random.randint(0, 60))
        }

        simulaciones.append(simulacion)

    return simulaciones