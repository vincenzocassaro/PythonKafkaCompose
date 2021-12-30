from flask import Flask, Response
from kafka import KafkaConsumer


app = Flask(__name__)

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    consumer = KafkaConsumer(topicname, bootstrap_servers='localhost:9092')
    def events():
        for msg in consumer:
            yield 'data:{0}\n\n'.format(msg)
    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=5001)