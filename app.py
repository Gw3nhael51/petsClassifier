from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

model = tf.keras.models.load_model("model.h5")
IMG_SIZE = (160, 160)

def preprocess(img_bytes):
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = image.img_to_array(img)
    arr = np.expand_dims(arr, axis=0)
    return arr

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    arr = preprocess(img_bytes)
    pred = model.predict(arr)[0][0]
    label = "Dog" if pred > 0.5 else "Cat"
    return {"prediction": label}
