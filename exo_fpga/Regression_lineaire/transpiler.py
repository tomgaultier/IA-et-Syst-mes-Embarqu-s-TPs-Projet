import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('houses.csv')
X = df[['size', 'nb_rooms', 'garden']]
y = df['price']
model = LinearRegression()
model.fit(X, y)


intercept = model.intercept_
coef = model.coef_

n_coef = len(coef)

code = """
`include "multiplieur_16bit.v"
`include "additionneur_32bit.v"

module regression_lineaire ("""

for i in range(n_coef):
    code += "x"+str(i)+","
code += "y);\n"


for i in range(n_coef):
    code += "input [15:0] x"+str(i)+";\n"

code += "\noutput [31:0] y;\n\n"

for i in range(n_coef):
    code += "wire [31:0] p"+str(i)+";\n"

for i in range(n_coef):
    code += "wire [31:0] s"+str(i)+";\n"
    
for i in range(n_coef):
    code += "multiplieur_16bit mult"+str(i)+"(" + str(coef[i]) + ", x" + str(i) + ", p" + str(i) +");\n"

code += "additionneur_32bit(" + str(intercept) + ", p0, 1'b0, s0 , rout);\n"

for i in range(n_coef-1):
    code += "additionneur_32bit add"+str(i)+"(s" + str(i)  + ", p" + str(i+1) + ", 1'b0, s" + str(i+1) +", rout);\n"
    
code += "assign y = s"+str(n_coef-1)+"\n"

code += "endmodule"

print(code)

# fichier = open("linear_regression.v",'w')
# fichier.write(code)
# fichier.close()