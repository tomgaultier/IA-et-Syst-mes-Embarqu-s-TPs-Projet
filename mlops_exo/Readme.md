# TP Transpiler

Ce TP a pour objectif de prendre un modèle de machine learning et de créer le code C affillié.

## Régression Linéaire

Dans le fichier "linear_regresion", vous trouverez le transpiler de la régression linéaire.
Faites d'abord exécuter le script **train_model.py** qui permettra de prendre les informations du fichiers **houses.csv** pour créer et entrainer un modèle de régression linéaire, qui sera sauvegarder par la librairie joblib dans le fichier **regression.joblib**.

Ensuite, vous avez le fichier principale, **transpile_simple_model.py**, qui récupère les coefficients du modèle, et crée le code C comprenant la fonction de détection. Le programme python fait ensuite une prédiction sur un set d'entrée avec la fonction predict.
Pour tester le programme en C, il suffit dans un premier temps de le compiler avec la commande : **gcc linear_regression.c -o linear_regression** dans l'invite de commande ouvert dans le chemin du programme. Puis de l'exécuter avec la commande : **linear_regression.exe**.

Le programme C va utiliser la fonction de prédiction créée avec les coefficients sur le même set d'entrée. Nous sommes supposés avoir le même résultat que la fonction predict de scikit-learn.

## Régression Logistique
