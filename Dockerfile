FROM python:3.10-slim

RUN apt-get clean && apt-get update && apt-get install -y curl

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python main.py"]
