import subprocess

def run(script):
    print(f"\n=== Running {script} ===")
    subprocess.run(["python", script], check=True)

if __name__ == "__main__":
    run("index.py")            # Préparation dataset
    run("clean_tf_images.py")  # renettoyer
    run("prepare_mixed.py")    # Création du dossier mixed
    run("train.py")            # Entraînement du modèle
    run("predict_random.py")    # Prédiction d'une image aléatoire

    print("\nPipeline completed successfully!")
