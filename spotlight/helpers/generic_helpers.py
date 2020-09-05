from flask import jsonify
from spotlight.helpers import constants as constants


def generic_error_response_with_code(exc, code=constants.ERROR_CODES["InternalServerError"]):
    return jsonify({"Error": {"Message": f"Exception raised while processing image: {exc}"}}), code
