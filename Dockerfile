FROM python:3.10-slim

RUN apt-get clean
RUN apt-get update
RUN apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false && poetry install --only main

COPY . .

CMD ["sh", "-c", "poetry run python main.py"]
