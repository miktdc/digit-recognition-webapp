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

# Make predictions on the test set
# predictions = model.predict(x_test)
# for i in range(x_test.size):
#     plt.imshow(x_test[i], cmap="gray")
#     plt.show()
#     print(f"Predicted label for test image {i}: {predictions[i].argmax()}")

# Load and preprocess a single image
file = './digits/4.png'
img = keras.preprocessing.image.load_img(file, target_size=(28, 28), color_mode='grayscale')
img_array = keras.preprocessing.image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0
img_array_inverted = 1.0 - img_array

prediction = model.predict(img_array_inverted)
digit = np.argmax(prediction)

print("Predicted Digit: ", digit)
for i, prob in enumerate(prediction[0]):
    print(f"Digit {i}: {prob}")
