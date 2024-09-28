# Usa una imagen base de tu elección (por ejemplo, Ubuntu)
FROM ubuntu:20.04

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    firefox \
    && rm -rf /var/lib/apt/lists/*

# Instala geckodriver
ENV GECKODRIVER_VERSION=0.32.0
RUN wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-linux64.tar.gz && \
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
