# Usar una imagen base de Python
FROM python:3.9-slim

# Instala dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libx11-xcb1 \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    libgbm-dev \
    libasound2 \
    libxrender1 \
    libxtst6 \
    libxrandr2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb-dev \
    libdbus-glib-1-2

# Instala Firefox
RUN apt-get install -y firefox-esr

# Instala GeckoDriver (WebDriver para Firefox)
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.31.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.31.0-linux64.tar.gz

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
CMD ["python", "noticias_cristianas.py"]
