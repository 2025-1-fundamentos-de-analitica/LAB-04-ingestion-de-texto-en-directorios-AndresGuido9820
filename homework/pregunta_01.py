# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import zipfile
import pandas as pd


def pregunta_01():
    """
    Descomprime el archivo input.zip y genera los archivos train_dataset.csv y test_dataset.csv
    en la carpeta output, con las columnas phrase y target.
    """
    input_zip_path = os.path.join("files", "input.zip")
    extract_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Descomprimir solo si no existe la carpeta
    if not os.path.exists(extract_dir):
        with zipfile.ZipFile(input_zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_dir)

    def build_dataset(split):
        data = []
        base_path = os.path.join(extract_dir, split)
        for sentiment in ["positive", "negative", "neutral"]:
            sentiment_path = os.path.join(base_path, sentiment)
            if not os.path.exists(sentiment_path):
                continue
            for fname in os.listdir(sentiment_path):
                fpath = os.path.join(sentiment_path, fname)
                if os.path.isfile(fpath):
                    with open(fpath, encoding="utf-8") as f:
                        phrase = f.read().strip()
                        data.append({"phrase": phrase, "target": sentiment})
        return pd.DataFrame(data)

    # Generar y guardar los datasets
    for split in ["train", "test"]:
        df = build_dataset(split)
        df.to_csv(os.path.join(output_dir, f"{split}_dataset.csv"), index=False)
