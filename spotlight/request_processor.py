import flask
from spotlight.helpers.generic_helpers import generic_error_response_with_code
from PIL import Image
import io


def process_lighten_request(app):
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            img = flask.request.files["image"]
            img = Image.open(img)

            img_stream = io.BytesIO()
            img.save(img_stream, format="PNG")
            img_stream.seek(0)

            response = app.response_class(img_stream, mimetype="image/png")
            response.headers.set('Content-Disposition', 'attachment', filename='result.png')
            return response
        else:
            return generic_error_response_with_code("Missing file")
    else:
        return generic_error_response_with_code("Bad method")
