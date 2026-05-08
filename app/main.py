from flask import Flask, request
import logging
import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route("/", methods=["GET", "POST"])
def main():
    logging.info("Ingestion runner triggered")

    return {
        "status": "SUCCESS",
        "message": "Ingestion service is running",
        "timestamp": str(datetime.datetime.utcnow())
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
