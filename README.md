# PythonKafkaCompose

PythonKafkaCompose is an upgrade of the amazing work done in [liveMaps](https://github.com/code-and-dogs/liveMaps) 

It is a simple project composed by:
-   an instance of Kafka (spinned with Docker-compose)
-   a Pyhton Consumer
-   a Python Producer

While I was studying the basic of Kafka I tried to follow what was done in liveMaps, but it was pretty outdated. So I went a step further and upgraded the infra using docker-compose and switched the library used to interact with kafka, from [PyKafka](https://pykafka.readthedocs.io/en/latest/) (archived) to [kafka-python](https://kafka-python.readthedocs.io/en/master/)

