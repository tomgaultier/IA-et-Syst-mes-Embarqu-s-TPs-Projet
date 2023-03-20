import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

code = ""
input_c = ""

def build_linear_model():
    df = pd.read_csv('houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "linear_regression.joblib")
    
def build_logistic_model():
    
    df = pd.read_csv('predictive_maintenance.csv')
    
    X = df[['vibration_db', 'average_speed', 'age', 'last_revision_date']]
    y = df['has_break_three_month_later']

    model = LogisticRegression()

    model.fit(X, y)

    joblib.dump(model, "logistic_regression.joblib")

def build_decision_tree_model():
      
    df = pd.read_csv('predictive_maintenance.csv')
    
    X = df.drop(columns="has_break_three_month_later")
    y = df['has_break_three_month_later']
    
    model = DecisionTreeClassifier(random_state=42, max_depth=20)
    
    model.fit(X, y)
    
    joblib.dump(model, "decision_tree.joblib")


def transpile_table(input_table):
    #conversion du tableau de test en tableau C avec les intersection 
    table_c = "{"
    for i, val in enumerate(input_table):
        table_c += str(val)  # ajoute la valeur actuelle à la chaîne
        if i != len(input_table) - 1:
            table_c += ", "  # ajoute une virgule et un espace si ce n'est pas la dernière valeur

    table_c += "}"  # ajoute une accolade fermante à la fin
    
    return table_c


def linear_regression():
    
    model = joblib.load("linear_regression.joblib")
    
    intercept = model.intercept_
    coefs = transpile_table(model.coef_)
    
    # tableau statique de test
    input_p = [[1, 2, 3]]
    
    input_c = transpile_table(input_p[0])
    
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
    
    return code, input_p, model


def logistic_regression():
    
    model = joblib.load("logistic_regression.joblib")
    
    intercept = model.intercept_
    coefs = transpile_table(model.coef_[0])
    
     # tableau statique de test
    input_p = [[1.7, 28.9, 76, 30]]
    
    input_c = transpile_table(input_p[0])
    
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
    
    return code, input_p, model

def get_code_from_tree(tree, class_names, input_c):
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

def decision_tree():
    
    model = joblib.load("decision_tree.joblib")
    
    # tableau statique de test
    input_p = [[1.7, 28.9, 76, 30]]
    
    input_c = transpile_table(input_p[0])
    
    class_names = model.classes_.tolist()    
    code = get_code_from_tree(model.tree_, class_names, input_c)
    
    return code, input_p, model


rep = input("Voulez vous faire :\nUne regression lineaire (1)\nUne regression logistique (2)\nUn arbre de decision (3)\n")

match rep:
    case "1":
        build_linear_model()
        code, input_p, model = linear_regression()
    case "2":
        build_logistic_model()
        code, input_p, model = logistic_regression()
    case "3":
        build_decision_tree_model()
        code, input_p, model = decision_tree()
        
    case other:
        print("pas de bonne reponse")
        exit()
    
fichier = open("regression.c",'w')
fichier.write(code)
fichier.close()

print("Compiler le script C : gcc regression.c -o regression, puis regression.exe")
print("Prediction avec la fonction predict sur le tableau : " + str(input_p) + "\n")
print(model.predict(input_p))    
    