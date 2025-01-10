from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from io import BytesIO
import keras
import numpy as np
from utils.preprocess import preprocess_image

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = keras.models.load_model("digits_model.keras")

@app.route("/predict", methods=["POST"])
def predict():
    print("Request received")
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = keras.preprocessing.image.load_img(BytesIO(file.read()), target_size=(28, 28), color_mode="grayscale")
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Invert the colors of the image array
    img_array_inverted = 1.0 - img_array

    prediction = model.predict(img_array_inverted)
    digit = np.argmax(prediction)
    print("Digit: ", digit)
    # prediction = model.predict(img_array)
    # digit = np.argmax(prediction)

    return jsonify({"prediction": int(digit)})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
