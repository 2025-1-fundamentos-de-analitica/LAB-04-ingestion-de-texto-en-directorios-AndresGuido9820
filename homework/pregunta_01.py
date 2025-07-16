# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""



import os
import shutil
import zipfile
import pandas as pd
from glob import glob


def pregunta_01():
    
    # ================================ #
    # Paso 1: Limpiar y descomprimir
    # ================================ #
    rutaC = "files/input.zip"
    rutaD = "input"

    if os.path.exists(rutaD):
        shutil.rmtree(rutaD)

    with zipfile.ZipFile(rutaC, "r") as zip_ref:
        zip_ref.extractall(".")

    # ================================ #
    # Paso 2: Crear carpeta de salida
    # ================================ #
    os.makedirs("files/output", exist_ok=True)

    # ================================ #
    # Paso 3: Procesar datos
    # ================================ #
    def procesarDatos(tipo):
        rutaBase = os.path.join(rutaD, tipo)
        datos = []
        for sentimiento in ["positive", "negative", "neutral"]:
            carpeta = os.path.join(rutaBase, sentimiento)
            for nombreArchivo in sorted(os.listdir(carpeta)):
                rutaArchivo = os.path.join(carpeta, nombreArchivo)
                with open(rutaArchivo, encoding="utf-8") as f:
                    texto = f.read().strip()
                    datos.append({
                        "phrase": texto,
                        "target": sentimiento
                    })
        return pd.DataFrame(datos)


   
    df_train = procesarDatos("train")
    df_test = procesarDatos("test")

    df_train.to_csv(os.path.join("files/output", "train_dataset.csv"), index=False)
    df_test.to_csv(os.path.join("files/output", "test_dataset.csv"), index=False)


if __name__ == "__main__":
    pregunta_01()