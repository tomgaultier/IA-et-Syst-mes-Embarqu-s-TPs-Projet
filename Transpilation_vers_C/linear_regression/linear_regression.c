
#include <stdio.h>
#include <stdlib.h>

float prediction(float* features, int n_feature){
    float intercept = -8152.937710156548;
    float coef[] = {717.2583697096838, 36824.195974256305, 101571.84002157037};
    float prediction = intercept;
    for (int i = 0; i < n_feature; i++) {
        prediction += features[i] * coef[i];
    }
    return prediction;
}

int main(){
    float data[3] =  {1, 2, 3};
    int n_features = sizeof(data)/sizeof(float);
    float prediction_result = prediction(data, n_features);
    printf("Prediction : %f", prediction_result);
    return 0; 
}
