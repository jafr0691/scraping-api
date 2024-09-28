# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /

# Copiar los archivos de requisitos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto en el que se ejecutará la API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
