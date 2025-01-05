FROM python:3.11-slim

WORKDIR /app

COPY /app /app/
COPY /app/requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

VOLUME ["/data"]

EXPOSE 3000

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]