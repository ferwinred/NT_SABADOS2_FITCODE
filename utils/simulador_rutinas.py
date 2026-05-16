import random
from datetime import datetime, timedelta

def generar_rutinas(num_rutinas):
    titulos = ["Entrenamiento de fuerza", "Yoga para principiantes", "Cardio intenso", "Entrenamiento funcional", "Baile fitness"]
    descripciones = ["Rutina enfocada en el desarrollo de fuerza y masa muscular. Ideal para quienes buscan progresar en levantamientos básicos y mejorar su rendimiento físico general.", "Rutina enfocada en el desarrollo de fuerza y masa muscular. Ideal para quienes buscan progresar en levantamientos básicos y mejorar su rendimiento físico general.", "Entrenamiento estructurado para trabajar todos los grupos musculares con cargas progresivas. Perfecto para niveles intermedios y avanzados.", "Sesiones de alta intensidad que combinan cardio y fuerza para maximizar la quema calórica en pocos minutos.", "Ejercicios suaves enfocados en la movilidad articular, flexibilidad y prevención de lesiones."]
    dificultades = ["fácil", "intermedio", "avanzado"]
    rutinas = []
    ahora = datetime.now()
    
    for _ in range(num_rutinas):
        
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