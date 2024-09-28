# Usa una imagen base de tu elección (por ejemplo, Ubuntu)
FROM ubuntu:20.04

# Configura la variable de entorno DISPLAY
ENV DISPLAY=:99

# Agrega cualquier otro archivo necesario y configuración
WORKDIR /
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "noticias_cristianas.py"]
