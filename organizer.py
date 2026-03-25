import os
import shutil

# Dossier à organiser
folder = input("Chemin du dossier à organiser : ")

# Extensions et dossiers associés
mapping = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDF": [".pdf"],
    "Textes": [".txt", ".md"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"],
}

# Création des dossiers si nécessaires
for folder_name in mapping.keys():
    path = os.path.join(folder, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)

# Tri des fichiers
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)

        for folder_name, extensions in mapping.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder, folder_name, filename))
                print(f"Déplacé : {filename} → {folder_name}")
                break

print("Organisation terminée !")
