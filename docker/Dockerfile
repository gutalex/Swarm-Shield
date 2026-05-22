FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sim/ ./sim/

# Запуск графического окна симулятора (понадобится проброс X11 или VNC)
CMD ["python", "sim/main_simulation.py"]