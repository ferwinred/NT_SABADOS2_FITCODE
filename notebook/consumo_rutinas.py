import requests

def consumo_rutinas():
    url = "http://localhost:8080/api/routines"

    response = requests.get(url)
    
    if response.status_code == 200:
        rutinas = response.json()
        return rutinas.get("content", [])
    else:
        print(f"Error al consumir la API: {response.status_code}")
        return None