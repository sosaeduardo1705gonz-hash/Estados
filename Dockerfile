# Imagen base
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY Estados.txt procesar.py index.html app.py /app/

# Instalar dependencias (si tuvieras requirements.txt)
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]

