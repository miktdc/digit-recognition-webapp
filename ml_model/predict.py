import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import numpy as np

# Load dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_test = keras.utils.normalize(x_test, axis=1)

# Load the pre-trained model
model = keras.models.load_model("digits_model.keras")

loss, accuracy = model.evaluate(x_test, y_test)

print("Loss: ", loss)
print("Accuracy: ", accuracy)

# predictions = model.predict(x_test)
# plt.imshow(x_test[0], cmap="gray")
# plt.show()
# print(f"Predicted label for first test image: {predictions[0].argmax()}")

file = './digits/digit9.png'
img = keras.preprocessing.image.load_img(file, target_size=(28, 28), color_mode='grayscale')
img_array = keras.preprocessing.image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Invert the colors of the image array
img_array_inverted = 1.0 - img_array

prediction = model.predict(img_array_inverted)
digit = np.argmax(prediction)

print("Digit: ", digit)
