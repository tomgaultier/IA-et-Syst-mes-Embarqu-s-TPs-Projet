# TP Transpiler

Ce TP a pour objectif de prendre un modèle de machine learning et de créer le code C affillié.

## Régression Linéaire

Dans le fichier **"linear_regresion"**, vous trouverez le transpiler de la régression linéaire.
Faites d'abord exécuter le script **train_model.py** qui permettra de prendre les informations du fichiers **houses.csv** pour créer et entrainer un modèle de régression linéaire, qui sera sauvegarder par la librairie joblib dans le fichier **regression.joblib**.

Ensuite, vous avez le fichier principale, **transpile_simple_model.py**, qui récupère les coefficients du modèle, et crée le code C comprenant la fonction de détection. Le programme python fait ensuite une prédiction sur un set d'entrée avec la fonction predict.
Pour tester le programme en C, il suffit dans un premier temps de le compiler avec la commande : **gcc linear_regression.c -o linear_regression** dans l'invite de commande ouvert dans le chemin du programme. Puis de l'exécuter avec la commande : **linear_regression.exe**.

Le programme C va utiliser la fonction de prédiction créée avec les coefficients sur le même set d'entrée. Nous sommes supposés avoir le même résultat que la fonction predict de scikit-learn.

## Régression Logistique

Vous trouverez dans le fichier **"logistic_regression"**, le transpiler de la régression logistique.
Sur le même principe que la régression linéaire, le code **train_model_logistic_regression.py** crée et entraine un modèle de régression logistique avec scikit-learn, d'après le csv **predictive_maintenance.csv**, qui le sauvegarde dans **logistic_regression.joblib**.
Une fois avoir crée le modèle, il faut exécuter le script **transpile_logistic_regression.py** générant le fichier **logistic_regression.c**. Il applique, avec les coefficients du modèle, une régression linéaire sur le set d'entrées, puis la fonction de coût Sigmoid.
Il ne reste plus qu'à compiler le programme avec la commande : **gcc logistic_regression.c -o logistic_regression**
Et de l'exécuter avec la commande : **logistic_regression.exe**

## Arbre de décision

Le transpiler de l'arbre de décision se trouve dans le fichier **"decision_tree" **.
Le code **train_model_decision_tree.py** crée le modèle d'arbre de décision à partir du csv **prédictive_maintenance.csv** et le stock dans le fichier joblib.
Le script **transpile_decision_tree** récupère le modèle et crée le code C de prédiction du modèle. Pour ce faire, on récupère toutes les branches de l'arbre, disponible dans la structure du modèle scikit-learn, et on crée des boucles selon le nombre de branches en mettant des conditions de poids sur chaque valeurs d'entrées (x1, x1,...) pour parcourir l'arbre.
Il faut ensuite compile le code C avec la commande : **gcc decision_tree.c -o decision_tree**
Et l'exécuter avec la commande : **decision_tree.exe**

## Transpiler des trois modèle

Dans le fichier **"Menu"**, vous trouverez un code qui demande à l' utilisateur s'il veut transpiler une régression linéaire, une régression logistique ou un arbre de décision.
Selon le choix, il fera la même chose que les codes précédents
