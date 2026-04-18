from utils.simulador_rutinas import generar_rutinas
import pandas as pd

rutinas = generar_rutinas(1000)

rutinas_ordenadas = pd.DataFrame(rutinas)

rutinas_ordenadas.to_json("data/rutinas.json", orient = "records", indent=4)

rutinas_ordenadas.to_csv("data/rutinas.csv")

print(rutinas_ordenadas)  # Imprime las primeras 5 rutinas generadas para verificar