FROM python:3.12-slim

WORKDIR /app

COPY consumer.py .

RUN pip install confluent-kafka

CMD ["python", "consumer.py"]