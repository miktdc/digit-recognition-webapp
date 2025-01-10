import tensorflow as tf
import matplotlib.pyplot as plt
import keras

# Load dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

# Load the pre-trained model
model = keras.models.load_model("digits_model.keras")

loss, accuracy = model.evaluate(x_test, y_test)

print("Loss: ", loss)
print("Accuracy: ", accuracy)