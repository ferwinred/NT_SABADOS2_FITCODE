from utils.simulacion_rachas import generar_rachas
from utils.simulacion_usuarios import generar_usuarios
from utils.simulacion_videos import generar_videos
import pandas as pd

usuarios = generar_usuarios(1000)

usuarios_ordenadas = pd.DataFrame(usuarios)

usuarios_ordenadas.to_json("data/simulaciones_usuarios.json", orient = "records", indent=4)

usuarios_ordenadas.to_csv("data/simulaciones_usuarios.csv")

videos = generar_videos(1000)

videos_ordenados = pd.DataFrame(videos)

videos_ordenados.to_json("data/simulaciones_videos.json", orient = "records", indent=4)

videos_ordenados.to_csv("data/simulaciones_videos.csv")

simulaciones=generar_rachas(1000)

simulaciones_ordenadas=pd.DataFrame(simulaciones)

simulaciones_ordenadas.to_json("data/simulaciones_rachas.json", orient="records", indent=4)

simulaciones_ordenadas.to_csv("data/simulaciones_rachas.csv") 
