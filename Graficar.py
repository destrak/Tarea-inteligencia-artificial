import pandas as pd
import matplotlib.pyplot as plt
import os

# Lista de archivos y sus etiquetas
archivos_info = [
    ("qlearning_ambiente1.txt", "Q-learning - Ambiente 1"),
    ("qlearning_ambiente2.txt", "Q-learning - Ambiente 2"),
    ("sarsa_ambiente1.txt", "SARSA - Ambiente 1"),
    ("sarsa_ambiente2.txt", "SARSA - Ambiente 2"),
]

# Leer, procesar y graficar cada archivo
for archivo, titulo in archivos_info:
    try:
        # Leer el archivo ignorando líneas vacías o no numéricas
        data = pd.read_csv(archivo, delim_whitespace=True, comment='#', header=None, names=["episodio", "reward"])
        
       
        data = data.sort_values(by="episodio")
        
        # Crear gráfico
        plt.figure(figsize=(10, 5))
        plt.scatter(data["episodio"], data["reward"], s=10)
        plt.title(titulo)
        plt.xlabel("Episodio")
        plt.ylabel("Reward acumulado")
        plt.grid(True)
        plt.axhline(y=0, color='black', linestyle='--')
        plt.tight_layout()
        
        # Guardar como imagen .png
        nombre_archivo_png = titulo.lower().replace(" ", "_").replace("-", "").replace("á", "a").replace("é", "e") + ".png"
        plt.savefig(nombre_archivo_png)
        print(f"Gráfico guardado como {nombre_archivo_png}")
        plt.close()

    except Exception as e:
        print(f"Error al procesar {archivo}: {e}")
