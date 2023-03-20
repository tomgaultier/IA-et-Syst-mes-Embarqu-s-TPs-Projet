import joblib
import numpy as np
from sklearn.linear_model import LinearRegression


model = joblib.load("regression.joblib")

intercept = model.intercept_
coef = model.coef_

#conversion des coefficients en tableau C avec les intersection 
coefs = "{"
for i, val in enumerate(coef):
    coefs += str(val)  # ajoute la valeur actuelle à la chaîne
    if i != len(coef) - 1:
        coefs += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

coefs += "}"  # ajoute une accolade fermante à la fin



# tableau statique de test
input = [[1, 2, 3]]

#conversion du tableau de test en tableau C avec les intersection 
input_c = "{"
for i, val in enumerate(input[0]):
    input_c += str(val)  # ajoute la valeur actuelle à la chaîne
    if i != len(input[0]) - 1:
        input_c += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

input_c += "}"  # ajoute une accolade fermante à la fin


# Redaction d'un script C avec une fonction de prediction en reprennant les coefficient du model actuel, et une fonction
# main pour lancer la predicition avec un tableau statique
code = f"""
#include <stdio.h>
#include <stdlib.h>

float prediction(float* features, int n_feature){{
    float intercept = {intercept};
    float coef[] = {coefs};
    float prediction = intercept;
    for (int i = 0; i < n_feature; i++) {{
        prediction += features[i] * coef[i];
    }}
    return prediction;
}}

int main(){{
    float data[3] =  {input_c};
    int n_features = sizeof(data)/sizeof(float);
    float prediction_result = prediction(data, n_features);
    printf("Prediction : %f", prediction_result);
    return 0; 
}}
"""


fichier = open("linear_regression.c",'w')
fichier.write(code)
fichier.close()

# On fait la prediction avec les mêmes données via la fonction "predict" pour regarder si notre code C renvoie la même reponse
print("Prediction avec le tableau : " + str(input) + "\n")
print(model.predict(input))

# Une fois le code python lancé, le fichier .c est créé. La compilation du script C se fait avec la commande :
# gcc linear_regression.c -o linear_regression
# Puis appeler le script avec la commande :
# linear_regression