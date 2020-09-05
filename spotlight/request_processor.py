import flask
from spotlight.helpers import constants as constants
from spotlight.helpers.generic_helpers import generic_error_response_with_code
import io
import spotlight.model_runner as model_runner
import tempfile
import logging
from werkzeug.utils import secure_filename
import os

logger = logging.getLogger("app")


class RequestProcessor(object):
    def __init__(self, app):
        self._app = app
        model_runner.load()

    def process_lighten_request(self):
        if flask.request.method == "POST":
            if flask.request.files.get("image"):
                dirpath = tempfile.mkdtemp()
                img = flask.request.files["image"]
                file_name = secure_filename(img.filename)
                img.save(os.path.join(dirpath, file_name))
                logger.info(f"Image {file_name} stored in temporary directory")

                try:
                    img_pil = model_runner.run(dirpath)
                except Exception as exc:
                    logger.error(f"Model crashed on image {file_name}: {exc}")
                    return generic_error_response_with_code(f"Model crashed when lightening the image {file_name}", constants.ERROR_CODES["InternalServerError"])
                img_stream = io.BytesIO()
                img_pil.save(img_stream, format="PNG")
                img_stream.seek(0)
                logger.info(f"Image {file_name} has been processed. Sending back to user..")

                response = self._app.response_class(img_stream, mimetype="image/png")
                response.headers.set('Content-Disposition', 'attachment', filename='result.png')
                return response
            else:
                logger.error("No file specified in request")
                return generic_error_response_with_code("Missing file", constants.ERROR_CODES["BadRequest"])
        else:
            logger.error("User tried other method than POST")
            return generic_error_response_with_code("Bad method", constants.ERROR_CODES["BadRequest"])
