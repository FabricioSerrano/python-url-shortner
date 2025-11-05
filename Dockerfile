FROM python:3.11-slim

RUN pip install --upgrade pip && pip install uv

WORKDIR /app

COPY ./shortner /app/shortner

COPY pyproject.toml uv.lock /app/

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "task", "prod"]