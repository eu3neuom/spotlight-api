from flask import jsonify


def generic_error_response_with_code(exc):
    return jsonify({"Error": {"Message": f"Exception raised while processing image: {exc}"}}), 500
