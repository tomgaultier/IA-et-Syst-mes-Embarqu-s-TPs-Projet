import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression


model = joblib.load("logistic_regression.joblib")

intercept = model.intercept_
coef = model.coef_

#conversion des coefficients en tableau C avec les intersection 
coefs = "{"
for i, val in enumerate(coef[0]):
    coefs += str(val)  # ajoute la valeur actuelle à la chaîne
    if i != len(coef[0]) - 1:
        coefs += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

coefs += "}"  # ajoute une accolade fermante à la fin



# tableau statique de test
input = [[1.7, 28.9, 76, 30]]

#conversion du tableau de test en tableau C avec les intersection 
input_c = "{"
for i, val in enumerate(input[0]):
    input_c += str(val)  # ajoute la valeur actuelle à la chaîne
    if i != len(input[0]) - 1:
        input_c += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

input_c += "}"  # ajoute une accolade fermante à la fin



code = f"""
#include <stdio.h>
#include <stdlib.h>

float exp_approx(float x, int n_term){{

    float result = 1.0;
    float term = 1.0;

    // x + x²/2 + x^3/6 + ... 
    for (int i = 1; i <= n_term; i++) {{
        term *= x / i;
        result += term;
    }}
    
    return result;
}}

float sigmoid(float x){{
    
    return 1/(1 + exp_approx(-x,10));
}}


float logistic_regression(float* features, int n_parameter){{
    
    float intercept = {intercept[0]};
    float coef[] = {coefs};
    float prediction = intercept;

    for(int i = 0; i < n_parameter; i++){{
        prediction += features[i] * coef[i+1];
    }}

    return sigmoid(prediction);
}}


int main(){{
    float features[4] =  {input_c};
    int n_features = sizeof(features)/sizeof(float);
    float prediction_result = logistic_regression(features, n_features);
    printf("Prediction : %f", prediction_result);
    return 0; 
}}
"""


fichier = open("logistic_regression.c",'w')
fichier.write(code)
fichier.close()

# On fait la prediction avec les mêmes données via la fonction "predict" pour regarder si notre code C renvoie la même reponse
print("Prediction avec le tableau : " + str(input) + "\n")
print(model.predict(input))

# Une fois le code python lancé, le fichier .c est créé. La compilation du script C se fait avec la commande :
# gcc logistic_regression.c -o logistic_regression
# Puis appeler le script avec la commande :
# logistic_regression