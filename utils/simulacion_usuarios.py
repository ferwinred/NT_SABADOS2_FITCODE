import random
from datetime import datetime, timedelta

def generar_simulacion(numeroSimulaciones):
    nombres = ["juan", "daniel", "fernando"]
    email = ["juan@gmail.com", "daniel@gmail.com", "fernando@gmail.com"]
    password_hash = ["hash1", "hash2", "hash3"]

    display_name = ["Juan Pérez", "Daniel García", "Fernando López"]
    simulaciones = []
    fechaInicio = datetime(1990, 1, 1)
    date_of_birth = random.randint(0, 365*30)  # Simula
    create_at = random.randint(0, 365*30)
    update_at = random.randint(0, 365*30)
    delete_at = random.randint(0, 365*30)
    role_id = [1, 2, 3]
    metadata = ["{}", "{}", "{}"]
    
    for _ in range(numeroSimulaciones):
        simulacion = {
            "id": random.randint(0, 200),
            "full_name": random.choice(nombres),
            "email": random.choice(email),
            "password_hash": random.choice(password_hash),
            "display_name": random.choice(display_name),
            "role_id": random.choice(role_id),
            "date_of_birth": fechaInicio + timedelta(days=random.randint(0, 365 * 30)),
            "sex": random.choice(["Masculino", "Femenino"]),
            "height_cm": random.randint(0, 250),
            "weight_kg": random.randint(0, 200),
            "metadata": random.choice(metadata),
            "created_at": fechaInicio + timedelta(days=random.randint(0, 365 * 30)),
            "updated_at": fechaInicio + timedelta(days=random.randint(0, 365 * 30)),
            "deleted_at": fechaInicio + timedelta(days=random.randint(0, 365 * 30))
        }

        simulaciones.append(simulacion)
    
    return simulaciones

