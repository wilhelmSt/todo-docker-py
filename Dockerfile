FROM python:3.11-slim

WORKDIR /app

COPY app/ /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/data"]

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]