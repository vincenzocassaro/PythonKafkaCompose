FROM python:3.7-alpine

WORKDIR /home/msadmin

COPY data/ data/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY producer.py .

ENTRYPOINT python producer.py