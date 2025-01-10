import numpy as np
from tensorflow import keras
from keras import preprocessing
from PIL import Image


def preprocess_image(file):
    img = Image.open(file).convert("L")
    img = img.resize((28, 28))
    img_array = preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array
