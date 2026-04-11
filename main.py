from utils.simulacion_usuarios import generar_simulacion
import pandas as pd

usuarios = generar_simulacion(1000)

usuarios_ordenadas = pd.DataFrame(usuarios)

usuarios_ordenadas.to_json("data/usuarios.json", orient = "records", indent=4)

usuarios_ordenadas.to_csv("data/usuarios.csv")

print(usuarios_ordenadas) 