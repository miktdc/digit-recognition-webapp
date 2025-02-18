import tensorflow as tf
import matplotlib.pyplot as plt
import keras

# Load dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

# Initialize the model
model = keras.models.Sequential()

# Turns the 28 x 28 grid into a flat 1 layer array of pixels
model.add(keras.layers.Flatten(input_shape=(28,28)))

# Dense layer: basic neural network layer where each neuron 
# is connected to each other neuron of the next layer
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(128, activation='relu'))

# Output layer with softmax
model.add(keras.layers.Dense(10, activation='softmax'))

# Compile the model with optimizer, loss function and metrics
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit/train the model
model.fit(x_train, y_train, epochs=12)

model.save('digits_model.keras')
