import csv

with open("Estados.txt", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    resultados = []
    for row in reader:
        estado = row["Estado"]
        temp = int(row["Temperatura"])
        humedad = int(row["Humedad"])
        costo_total = int(row["Costo_Alojamiento"]) + int(row["Costo_Transporte"])
        resultados.append(f"{estado}: Temp={temp}°C, Humedad={humedad}%, Costo={costo_total}")

with open("resultado.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(resultados))

