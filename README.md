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

1) Spin up Architecture (Zookeper and Kafka) and Services (Consumer and Producer)

```
docker-compose up -d
```

The consumer is a Flask app that expose and endpoint on localhost:5000

so open the browser and go to localhost:5000/topic/test to see a stream of string coming from the topic

---

## Known Issues

The Produces will go down a couple of times, because the Architecture is not ready yet.
One possible solution is to use the scripts in the scripts folder to first spin up the Architecture and, once ready, spin up the services

---

## Roadmap

[X] Dockerize Consumer

[X] Dockerize Producer

[ ] Use a Makefile to run startup scripts

[ ] Add an external consumer and producer

[ ] Flask -> FastApi

[ ] Use Poetry

[ ] Think about include https://ntfy.sh/

[ ] Add a Spark Streaming example for fun?
