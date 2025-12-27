import shutil
import random
from pathlib import Path

SOURCE = Path("test")  # on mélange les images du dossier test
MIXED = Path("mixed")

MIXED.mkdir(exist_ok=True)

def collect_images():
    cats = list((SOURCE / "Cat").glob("*.jpg"))
    dogs = list((SOURCE / "Dog").glob("*.jpg"))
    return cats + dogs

def create_mixed_folder():
    images = collect_images()
    random.shuffle(images)

    for img in images:
        shutil.copy(img, MIXED / img.name)

    print(f"Mixed folder created with {len(images)} images.")

if __name__ == "__main__":
    create_mixed_folder()
