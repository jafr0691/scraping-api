# Usa una imagen base de tu elección (por ejemplo, Ubuntu)
FROM ubuntu:20.04

# Actualiza e instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    libxrender1 \
    libasound2 \
    libglib2.0-0 \
    xvfb \
    firefox \
    && rm -rf /var/lib/apt/lists/*

# Descarga e instala GeckoDriver
RUN GECKODRIVER_VERSION=0.32.0 && \
    wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-linux64.tar.gz && \
    tar -xzf geckodriver-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-linux64.tar.gz

# Configura la variable de entorno DISPLAY
ENV DISPLAY=:99

# Agrega cualquier otro archivo necesario y configuración
WORKDIR /
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "noticias_cristianas.py"]
