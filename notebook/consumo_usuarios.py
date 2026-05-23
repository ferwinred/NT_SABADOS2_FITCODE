import requests

def consumo_usuarios():
    url = "http://localhost:8080/api/users"
    response = requests.get(url)
    
    if response.status_code == 200:
        usuarios = response.json()
        return usuarios
    else:
        print(f"Error al consumir la API: {response.status_code}")
        return None