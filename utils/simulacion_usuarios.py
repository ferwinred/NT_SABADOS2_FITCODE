import random
from datetime import datetime, timedelta

def generar_usuarios(numeroSimulaciones):
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
            "fullName": random.choice(nombres),
            "email": random.choice(email),
            "passwordHash": random.choice(password_hash),
            "displayName": random.choice(display_name),
            "role": random.choice(role_id),
            "dateOfBirth": fechaInicio + timedelta(days=random.randint(0, 365 * 30)),
            "sex": random.choice(["Masculino", "Femenino"]),
            "heightCm": random.randint(0, 250),
            "weightKg": random.randint(0, 200),
            "metadata": random.choice(metadata),
            "createdAt": fechaInicio + timedelta(days=random.randint(0, 365 * 30)),
            "updatedAt": fechaInicio + timedelta(days=random.randint(0, 365 * 30))
        }

        simulaciones.append(simulacion)
    
    return simulaciones

