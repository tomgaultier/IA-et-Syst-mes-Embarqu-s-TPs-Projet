
#include <stdio.h>
#include <stdlib.h>

float exp_approx(float x, int n_term){

    float result = 1.0;
    float term = 1.0;

    // x + x²/2 + x^3/6 + ... 
    for (int i = 1; i <= n_term; i++) {
        term *= x / i;
        result += term;
    }
    
    return result;
}

float sigmoid(float x){
    
    return 1/(1 + exp_approx(-x,10));
}


float logistic_regression(float* features, int n_parameter){
    
    float intercept = -145.04756383895904;
    float coef[] = {1.3646112003685942, 0.5982646355181507, 0.9185351918158191, 0.15823597631930084};
    float prediction = intercept;

    for(int i = 0; i < n_parameter; i++){
        prediction += features[i] * coef[i+1];
    }

    return sigmoid(prediction);
}


int main(){
    float features[4] =  {1.7, 28.9, 76, 30};
    int n_features = sizeof(features)/sizeof(float);
    float prediction_result = logistic_regression(features, n_features);
    printf("Prediction : %f", prediction_result);
    return 0; 
}
