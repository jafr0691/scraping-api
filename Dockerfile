# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar dependencias necesarias, incluyendo wget y Firefox
RUN apt-get update && apt-get install -y \
    wget \
    firefox-esr

# Descargar e instalar geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.30.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.30.0-linux64.tar.gz

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto en el que se ejecutará la API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "noticias_cristianas.py"]
