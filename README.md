# PythonKafkaCompose

PythonKafkaCompose is an upgrade of the amazing work done in [liveMaps](https://github.com/code-and-dogs/liveMaps) 

It is a simple project composed by:
- an instance of Kafka
- a Python Consumer
- a Python Producer

### Key Differencies

- upgraded the infra using docker-compose 
- switched the library used to interact with kafka, from [PyKafka](https://pykafka.readthedocs.io/en/latest/) (archived) to [kafka-python](https://kafka-python.readthedocs.io/en/master/)

---

## Getting Started

1) Spin up Zookeper and Kafka

```
docker-compose up -d
```

2) Setup environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3) Run the Producer
```
python producer.py
```

4) Run the Consumer (in a new terminal)
```
python consumer.py
```
The consumer is a Flask app that expose and endpoint on localhost:5001

so open the browser and go to localhost:5001/topic/topic_test to see a stream of string coming from the topic

---

## Roadmap

[WIP] Dockerize Consumer

[ ] Dockerize Producer

[ ] Flask -> FastApi

[ ] Use Poetry

[ ] Think about include https://ntfy.sh/
