"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re
import os
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

      

    """
    
    path="files/input/clusters_report.txt"
    with open(path, encoding="utf-8") as f:
        raw_lines = [ln.rstrip("\n") for ln in f]

    lines = [ln for ln in raw_lines if ln.strip() != ""]

    header_idxs = [i for i, ln in enumerate(lines) if re.match(r"^\s*\d+\s+\d+\s+[\d,]+\s*%\s*", ln)]

    rows = []
    for idx_pos, idx in enumerate(header_idxs):
        header = lines[idx]
        m = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)$", header)
        if not m:
            continue
        cluster = int(m.group(1))
        cantidad = int(m.group(2))
        porcentaje = float(m.group(3).replace(",", "."))
        keywords = m.group(4).strip()

        start = idx + 1
        end = header_idxs[idx_pos + 1] if idx_pos + 1 < len(header_idxs) else len(lines)
        if start < end:
            extra = " ".join(lines[start:end]).strip()
            if extra:
                keywords = (keywords + " " + extra).strip()

        keywords = re.sub(r"\s*,\s*", ", ", keywords)
        keywords = re.sub(r"\s+", " ", keywords).strip()
        if keywords.endswith("."):
            keywords = keywords[:-1].strip()

        rows.append({
            "cluster": cluster,
            "cantidad_de_palabras_clave": cantidad,
            "porcentaje_de_palabras_clave": porcentaje,
            "principales_palabras_clave": keywords
        })

    return pd.DataFrame(rows)


# rpta=pregunta_01()
# print(rpta)