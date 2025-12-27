import tensorflow as tf
from pathlib import Path

def is_tf_valid(path: Path) -> bool:
    try:
        img_bytes = tf.io.read_file(str(path))
        tf.image.decode_jpeg(img_bytes)
        return True
    except:
        return False

def clean_folder(folder: Path):
    removed = 0
    for img in folder.glob("*.jpg"):
        if not is_tf_valid(img):
            img.unlink()
            removed += 1
    return removed

if __name__ == "__main__":
    total_removed = 0
    for label in ["Cat", "Dog"]:
        total_removed += clean_folder(Path("train") / label)
        total_removed += clean_folder(Path("test") / label)

    print(f"Removed {total_removed} corrupted images.")
