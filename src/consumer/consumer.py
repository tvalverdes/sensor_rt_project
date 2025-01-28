import os

from confluent_kafka import Consumer, KafkaError

BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "test-topic")
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "group_id")
consumer = Consumer(
    {
        "bootstrap.servers": BROKER,
        "group.id": GROUP_ID,
        "auto.offset.reset": "earliest",
    }
)

consumer.subscribe([TOPIC])

try:
    while True:
        msg = consumer.poll()
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print(f'Received message: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
