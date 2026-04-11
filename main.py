from utils.simulacion_rachas import generar_simulacion
from utils.simulacion_usuarios import generar_simulacion
import pandas as pd

usuarios = generar_simulacion(1000)

usuarios_ordenadas = pd.DataFrame(usuarios)

usuarios_ordenadas.to_json("data/usuarios.json", orient = "records", indent=4)

usuarios_ordenadas.to_csv("data/usuarios.csv")


simulaciones=generar_simulacion(5)


simulaciones_ordenadas=pd.DataFrame(simulaciones)

#crear una funcion generica que convierta cualquier simulacion ordenada en un json 
#convirtiendo nuestras simulaciones en dos formas diferentes 
#json
simulaciones_ordenadas.to_json("data/simulaciones_ordenadas.json", orient="records", indent=4)
#csv
simulaciones_ordenadas.to_csv("data/simulacions.csv") 
