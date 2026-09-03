import os
import shutil

telechargements = "/Users/macbookair/Downloads"

dossiers = {
    "Image" : [".jpg", ".jpeg", ".png",".gif",".bmp"],
    "Videos" : [".mp4", ".mkv", ".avi", ".mov"],
    "Documents" : [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Musique" : [".mp3", ".wav", ".flac"],
    "Archives" : [".zip", ".rar", ".tar", ".gz"],
    "Scripts" : [".py", ".sh", ".js", ";html", ".css"]
}

for dossier in dossiers :
    path = os.path.join(telechargements, dossier)
    if not os.path.exists(path):
        os.makedirs(path)

for nom_fichier in os.listdir(telechargements):
    file_path = os.path.join(telechargements, nom_fichier)

    if os.path.isdir(file_path):
        continue

    for dossier, extensions in dossiers.items():
        if nom_fichier.lower().endswith(tuple(extensions)):
            shutil.move(file_path, os.path.join(telechargements, dossier, nom_fichier)) 
            print(f"Déplacé : {nom_fichier} -> {dossier}")
            break       


