FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .  # Copy requirements first to leverage Docker cache
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
