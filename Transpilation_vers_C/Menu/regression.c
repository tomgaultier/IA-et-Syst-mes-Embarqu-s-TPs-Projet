#include <stdio.h>
#include <stdlib.h>
int simple_tree(float* features) {
if (features[2] <= 129.5) {
    if (features[2] <= 122.5) {
        return 0;
    }
    else {
        if (features[3] <= 65.5) {
            return 0;
        }
        else {
            if (features[0] <= 0.745822548866272) {
                if (features[1] <= 30.26838779449463) {
                    return 0;
                }
                else {
                    return 1;
                }
            }
            else {
                return 1;
            }
        }
    }
}
else {
    if (features[2] <= 132.5) {
        if (features[0] <= 0.9077316522598267) {
            return 0;
        }
        else {
            return 1;
        }
    }
    else {
        if (features[2] <= 134.5) {
            if (features[0] <= 0.7520483434200287) {
                return 0;
            }
            else {
                return 1;
            }
        }
        else {
            return 1;
        }
    }
}
}
int main(){
        float features[4] =  {1.7, 28.9, 76, 30};
        int prediction_result = simple_tree(features);
        printf("Prediction : %d", prediction_result);
        return 0; 
    }