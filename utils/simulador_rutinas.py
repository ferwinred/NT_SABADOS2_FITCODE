import random
from datetime import datetime, timedelta

def simular_servicios(num_servicios):
    titulos = ["Entrenamiento de fuerza", "Yoga para principiantes", "Cardio intenso", "Entrenamiento funcional", "Baile fitness"]
    descripciones = ["motilada", "desparasitada", "vacunacion", "esterilizacion", "corte de uñas"]
    dificultades = ["fácil", "intermedio", "avanzado"]
    rutinas = []
    ahora = datetime.now()
    
    for _ in range(num_servicios):
        
        created_at = ahora - timedelta(days=random.randint(0, 30))
        updated_at = created_at + timedelta(days=random.randint(0, 10))
        
        rutina = {
            "id": random.randint(1, 10000),
            "title": random.choice(titulos),
            "description": random.choice(descripciones),
            "difficulty": random.choice(dificultades),
            "duration_minutes": random.randint(10, 120),
            "author_user_id": random.randint(1, 100),  # debe existir en users
            "is_public": random.choice([0, 1]),
            "metadata": {
                "calories_estimate": random.randint(100, 800),
                "equipment": random.choice(["none", "dumbbells", "full gym"]),
                "recommended": random.choice([True, False])
            },
            "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        rutinas.append(rutina)
    return rutinas