import os
from pathlib import Path
import shutil
from sklearn.model_selection import train_test_split
from PIL import Image
from tqdm import tqdm

# Dossier source
data = Path('data/PetImages')

# Dossiers de sortie
train = Path('train')
test = Path('test')

# Création des dossiers train/test
for folder in ['Cat', 'Dog']:
    (train / folder).mkdir(parents=True, exist_ok=True)
    (test / folder).mkdir(parents=True, exist_ok=True)

# Fonction de validation d'image
def is_valid_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

# Récupération et nettoyage des images
def load_and_clean_images(label: str):
    folder = data / label
    files = list(folder.glob('*.jpg'))
    valid = []

    print(f"Checking {label} images...")
    for file in tqdm(files):
        if file.is_file() and is_valid_image(file):
            valid.append(file)

    return valid

cat_images = load_and_clean_images('Cat')
dog_images = load_and_clean_images('Dog')

print(f"Valid images — Cats: {len(cat_images)}, Dogs: {len(dog_images)}")

# Split
train_cats, test_cats = train_test_split(cat_images, test_size=0.2, random_state=42)
train_dogs, test_dogs = train_test_split(dog_images, test_size=0.2, random_state=42)

# Copie des fichiers avec tqdm
def copy_images(images, destination: Path, label: str):
    print(f"Copying {label} images...")
    for img in tqdm(images):
        shutil.copy(img, destination / img.name)

copy_images(train_cats, train / 'Cat', "train/Cat")
copy_images(test_cats, test / 'Cat', "test/Cat")
copy_images(train_dogs, train / 'Dog', "train/Dog")
copy_images(test_dogs, test / 'Dog', "test/Dog")

print("Split completed!")
