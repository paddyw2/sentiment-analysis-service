from flask import Flask, jsonify, request
import predict as ml_predict
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/ht", methods=["GET"])
def healthcheck():
    status = {"status": 200}
    return jsonify(status)


@app.route("/predict", methods=["POST"])
def predict():
    text_to_predict = request.json["text"]
    logger.debug("Received: %s" % text_to_predict)
    prediction = ml_predict.predict_sentiment(text_to_predict)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
