import random
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

MODEL = "model.h5"
IMG_SIZE = (160, 160)

model = tf.keras.models.load_model(MODEL)

mixed = Path("mixed")
images = list(mixed.glob("*.jpg"))

img_path = random.choice(images)
print(f"Predicting: {img_path.name}")

img = image.load_img(img_path, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

prediction = model.predict(img_array)[0][0]

label = "Dog" if prediction > 0.5 else "Cat"
print(f"Prediction: {label}")
