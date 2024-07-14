from app import app, logging, log_level
from api_endpoints import lm_studio
from api_endpoints import ollama

from os import environ

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info("Starting the web server")
    is_debug = log_level in ["INFO", "DEBUG"]
    HOST = environ.get("HOST", "0.0.0.0")
    PORT = int(environ.get("PORT", "3214"))
    app.run(debug=is_debug, host=HOST, port=PORT)
