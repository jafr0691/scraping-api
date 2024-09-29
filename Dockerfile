FROM --platform=linux/amd64 python:3.9-slim-buster

# Install Firefox and other dependencies
RUN apt-get update && apt-get install -y firefox-esr xvfb python3-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Set the PATH to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages inside the virtual environment
RUN pip install --upgrade pip
RUN pip install selenium flask webdriver_manager

# Copy Python script
COPY noticias_cristianas.py .

ENV DISPLAY=:99

# Run script with xvfb
CMD ["xvfb-run", "--server-args='-screen 0 1024x768x24'", "--auto-servernum", "python", "noticias_cristianas.py"]
