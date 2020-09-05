from flask import Flask, jsonify

from spotlight import request_processor

app = Flask(__name__)


@app.route("/spotlight/api/v1.0/lighten", methods=["POST"])
def lighten():
    return request_processor.process_lighten_request(app)


if __name__ == '__main__':
    app.run()
