import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

model = joblib.load("decision_tree.joblib")

# tableau statique de test
input = [[1.7, 28.9, 76, 30]]

#conversion du tableau de test en tableau C avec les intersection 
input_c = "{"
for i, val in enumerate(input[0]):
    input_c += str(val)  # ajoute la valeur actuelle à la chaîne
    if i != len(input[0]) - 1:
        input_c += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

input_c += "}"  # ajoute une accolade fermante à la fin



def get_code_from_tree(tree, feature_names, class_names):
    code = ""

    def recurse(code, node, depth):
        indent = "    " * depth
        if tree.feature[node] == -2:
            code += "{}return {};\n".format(indent, class_names[np.argmax(tree.value[node])])
        else:
            code += "{}if (features[{}] <= {}) {{\n".format(indent, tree.feature[node], tree.threshold[node])
            code = recurse(code, tree.children_left[node], depth + 1)
            code += "{}}}\n".format(indent)
            code += "{}else {{\n".format(indent)
            code = recurse(code, tree.children_right[node], depth + 1)
            code += "{}}}\n".format(indent)
        return code
    
    code = recurse(code, 0, 0)
    function_name = "simple_tree"
    arguments = "float* features"
    code = "#include <stdio.h>\n#include <stdlib.h>\nint {}({}) {{\n".format(function_name, arguments) + code + "}\n"

    code += """int main(){{
        float features[4] =  {};
        int prediction_result = simple_tree(features);
        printf("Prediction : %d", prediction_result);
        return 0; 
    }}""".format(input_c)
    
    return code



feature_names = model.tree_.feature
class_names = model.classes_.tolist()

code = get_code_from_tree(model.tree_, feature_names, class_names)


fichier = open("decision_tree.c",'w')
fichier.write(code)
fichier.close()

# On fait la prediction avec les mêmes données via la fonction "predict" pour regarder si notre code C renvoie la même reponse
print("Prediction avec le tableau : " + str(input) + "\n")
print(model.predict(input))

# Une fois le code python lancé, le fichier .c est créé. La compilation du script C se fait avec la commande :
# gcc decision_tree.c -o decision_tree
# Puis appeler le script avec la commande :
# decision_tree