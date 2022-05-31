from flask import Flask, Response
from kafka import KafkaConsumer
import time

app = Flask(__name__)


@app.route("/healtcheck")
def healtcheck():
    return {"health": "ok", "time": time.time()}


# Consumer API
@app.route("/topic/<topicname>")
def get_messages(topicname):
    consumer = KafkaConsumer(topicname, bootstrap_servers="kafka:9093")

    def events():
        for msg in consumer:
            yield "data:{0}\n\n".format(msg)

    return Response(events(), mimetype="text/event-stream")


# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
