# Projet_Maths_Kivy

Utilisation du code :

Mettre tout le dossier Script_Monty_Kivy dans un dossier sur votre ordinateur (main.py + android.kv + Images) et lancer le main.py directement en ayant au préalable installé les bibliothèques importées au début du fichier main.py (soit kivy et numpy)



Buildozer :

Installer virtualenv cython kivy (voir versions requises sur le site de la documentation de buildozer) Et QUE JAVA 8 de préférence


Dans le dossier où on a le main.py et le .kv, on lance un terminal et on tape:

Buildozer init
= > Crée un .spec

Remplir le .spec comme dans les tutos sur internet
comme par exemple le titre, le domaine, la version, les images d'icônes, fullscreen, landscape/portrait, les bibliothèques android…

Buildozer android debug (+deploy run) (+logcat)
Buildozer installe automatiquement les outils d'Android (api ndk sdk) indiqués dans le .spec

Crée le .apk dans le dossier bin et l'installe (la push) si on a dit déploy run
