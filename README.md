# 🐶🐱 Cats vs Dogs Classifier

A complete image classification project with a modern web interface (Tailwind v4) and a FastAPI backend. Includes a full ML pipeline: dataset preparation, training, inference, and a drag-and-drop UI.

---

## 🚀 Features

### 🔍 **Machine Learning**
- MobileNetV2 transfer learning
- Clean training pipeline (augmentation, split, reproducibility)
- Exported model (`.h5`)
- Supports 3 classes: **cat**, **dog**, **other** (optional)

### 🖥️ **Backend (FastAPI)**
- `/predict` endpoint for image inference
- Handles file uploads
- Returns JSON predictions
- Lightweight and fast

### 🎨 **Frontend (Tailwind v4)**
- Modern UI with glassmorphism
- Drag & drop image upload
- Live preview before prediction
- Responsive and clean design

---

## 📁 Project Structure

```plaintext
learn_Ai/
│
├── app.py                                # FastAPI backend
├── train.py                              # Model training script
├── predict_random.py                     # Quick prediction test
├── prepare_mixed.py                      # Dataset preparation
├── clean_tf_images.py                    # Dataset cleaning
├── transformh5.py                        # Model conversion utilities
│
├── static/
│   ├── index.html                        # Web interface
│   ├── tailwind.css                      # Tailwind input
│   └── style.css                         # Generated CSS
│
├── tailwindcss                           # Tailwind v4 standalone binary
└── model.h5                              # Trained model (ignored by Git)
```

---

## 🧪 Training the Model

```bash
python train.py
```

This script:
- Loads and cleans the dataset
- Applies augmentation
- Trains MobileNetV2
- Saves the model as `model.h5`

---

## 🖼️ Running the Web App

1. **Start Tailwind (watch mode):**
   ```bash
   ./tailwindcss -i ./static/tailwind.css -o ./static/style.css --watch
   ```

2. **Start FastAPI:**
   ```bash
   uvicorn app:app --reload
   ```

3. **Open the UI:**
   Visit [http://localhost:8000](http://localhost:8000), upload an image, and get a prediction instantly.

---

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Gw3nhael51/petsClassifier.git
   cd petsClassifier
   ```

2. **Create a virtual environment:**

   **Linux/macOS (or WSL on Windows):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Future Improvements
- Add confidence scores
- Add more classes (fox, wolf, etc.)
- Deploy online (Render, Railway, HuggingFace Spaces)
- Add webcam live prediction

---

## 📜 License
MIT License.

---

## ✨ Author
Gwenhael — ML & Web Developer