from flask import Flask, jsonify

from spotlight.request_processor import RequestProcessor
from spotlight.helpers.generic_helpers import generic_error_response_with_code
import spotlight.helpers.constants as constants
import logging

logger = logging.getLogger("app")
app = Flask(__name__)
request_processor = RequestProcessor(app)


@app.route("/spotlight/api/v1.0/lighten", methods=["POST"])
def lighten():
    try:
        return request_processor.process_lighten_request()
    except Exception as exc:
        logger.error(f"Error while processing request: {exc}")
        return generic_error_response_with_code(
            f"Internal server error", constants.ERROR_CODES["InternalServerError"]
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
