FROM --platform=linux/amd64 python:3.9-slim-buster

# Actualizar e instalar Firefox, xvfb, xauth, y otras dependencias necesarias
RUN apt-get update && apt-get install -y \
    firefox-esr \
    xvfb \
    xauth \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
# Verificar la ubicación de firefox-esr
RUN which firefox-esr
# Instalar paquetes de Python necesarios
RUN pip install --no-cache-dir selenium flask webdriver_manager

# Copiar el script de Python a la imagen
COPY noticias_cristianas.py .

# Configurar la variable de entorno DISPLAY
ENV DISPLAY=:99

# Comando para ejecutar el script con xvfb
CMD ["xvfb-run", "--server-args=-screen 0 1024x768x24", "python", "noticias_cristianas.py"]
