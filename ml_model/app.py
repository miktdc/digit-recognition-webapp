from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from utils.preprocess import preprocess_image

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = tf.keras.models.load_model("model/digit_model.h5")


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img_array = preprocess_image(file)

    prediction = model.predict(img_array)
    digit = np.argmax(prediction)

    return jsonify({"prediction": int(digit)})


if __name__ == "__main__":
    app.run(debug=True)
