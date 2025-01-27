FROM python:3.12-slim

WORKDIR /app

COPY producer.py .

RUN pip install confluent-kafka Faker

CMD ["python", "producer.py"]