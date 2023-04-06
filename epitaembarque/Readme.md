## Entraînement du modèle

Dans le notebook, vous trouverez l'entraînement d'un modèle de classification de chiffre mnist.
Plusieurs modèles sont créés, notamment avec quantification, pour obtenir la meilleur précision avec le modèle le plus léger possible afin de le mettre sur une Arduino.

## Intégration sur Arduino

En reprenant l'exemple de la bibliothèque tflite de L'IDE Arduino, le code récupère le modèle de classification que j'ai mis en format .h dans le notebook. Il prend en boucle une photo avec la caméra OV7675 et fait une prédiction de ce qui est vue.
Pour déterminer le chiffre prédit, on regarde la précision correspondant à la prédiction de chaque chiffre, on choisit celui qui a la meilleur précision. Ce sera le chiffre qui sera le plus probable d'être prédit.
Malheureusement, malgré de nombreux essais et recherches, je rentre toujours dans l'erreur **Invoke failed**, comme si je n'allouait pas le bon nombre de mémoire pour le modèle.
A part cela, je n'ai pas d'autres problèmes. Mais la prédiction reste donc à zéro étant donné que le modèle ne veut pas se mettre en place. 
