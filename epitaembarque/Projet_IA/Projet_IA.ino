#include <Arduino_OV767X.h>

#include <Arduino.h>
#include <TensorFlowLite.h>

#include <OV767X.h>
#include <Wire.h>
#include <SD.h>

#include "main_functions.h"

#include "detection_responder.h"
#include "image_provider.h"
#include "model_settings.h"
#include "person_detect_model_data.h"
#include "tensorflow/lite/micro/micro_error_reporter.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"

unsigned short pixels[176 * 144]; // QCIF: 176x144 X 2 bytes per pixel (RGB565)



// Initialiser la caméra
OV767X camera;

// Définissez le chemin du fichier .tflite sur votre carte SD ou Flash
const char* model_path = "/qat_model_quantized.tflite";

// Définir la taille du tampon d'entrée et de sortie du modèle
const int input_size = 784;
const int output_size = 10;

// Initialiser les tampons d'entrée et de sortie du modèle
float input_buffer[input_size];
float output_buffer[output_size];

// Créer un objet TensorFlowLite pour charger et exécuter le modèle
tflite::Interpreter* interpreter;

// Définir la fonction de configuration du modèle
void setupModel() {
  // Charger le modèle depuis la carte SD ou Flash
  File model_file = SD.open(model_path);
  size_t model_size = model_file.size();
  std::unique_ptr<uint8_t[]> model_buffer(new uint8_t[model_size]);
  model_file.read(model_buffer.get(), model_size);

  // Créer un objet de résolution de modèle
  tflite::ops::builtin::BuiltinOpResolver resolver;

  // Créer un objet TensorFlowLite pour charger et exécuter le modèle
  tflite::MicroInterpreter* static_interpreter(
      model_buffer.get(), resolver, nullptr, nullptr);
  micro_interpreter = &static_interpreter;
  // Allouer de la mémoire pour les tampons d'entrée et de sortie du modèle
  TfLiteStatus allocate_status = micro_interpreter->AllocateTensors();
  if (allocate_status != kTfLiteOk) {
    Serial.println("Erreur lors de l'allocation des tampons de modèle.");
    return;
  }

  // Enregistrer les tampons d'entrée et de sortie du modèle
  interpreter = micro_interpreter->interpreter();
  TfLiteTensor* input_tensor = interpreter->input(0);
  input_tensor->data.f = input_buffer;
  TfLiteTensor* output_tensor = interpreter->output(0);
  output_tensor->data.f = output_buffer;

  Serial.println("Le modèle est prêt.");
}

// Définir la fonction d'inférence du modèle
int runModel(float* input) {
  // Copier les données d'entrée dans le tampon d'entrée du modèle
  memcpy(input_buffer, input, input_size * sizeof(float));

  // Exécuter le modèle
  interpreter->Invoke();

  // Trouver la sortie la plus probable
  int max_index = 0;
  for (int i = 1; i < output_size; i++) {
    if (output_buffer[i] > output_buffer[max_index]) {
      max_index = i;
    }
  }

  // Retourner la classe prédite
  return max_index;
}

void setup() {
  // Initialiser la communication série
  Serial.begin(9600);
  while (!Serial);

  Serial.println("OV767X Camera Capture");
  Serial.println();

  if (!Camera.begin(QCIF, RGB565, 1)) {
    Serial.println("Failed to initialize camera!");
    while (1);
  }

  // Initialiser la carte SD
  if (!SD.begin()) {
    Serial.println("Impossible d'initialiser la carte SD.");
    return;
  }

  // Configurer le modèle
  setupModel();

}

void loop() {
  // Capturer une image de la caméra
  Camera.readFrame(pixels);

  // Convertir l'image en niveaux de gris et la redimensionner
  int image_size = Camera.width() * Camera.height();
  uint8_t gray_image[image_size];
  for (int i = 0; i < image_size; i++) {
    uint8_t r = pixels[i * 2];
    uint8_t g = pixels[i * 2 + 1];
    uint8_t b = (r * 38 + g * 75 + b * 15) >> 7;
    gray_image[i] = b;
  }
  uint8_t resized_image[input_size];
  for (int i = 0; i < input_size; i++) {
    int x = i % 28;
    int y = i / 28;
    int xx = x * Camera.width() / 28;
    int yy = y * Camera.height() / 28;
    resized_image[i] = gray_image[yy * Camera.width() + xx];
  }

  // Normaliser l'image et l'envoyer au modèle pour inférence
  float normalized_image[input_size];
  for (int i = 0; i < input_size; i++) {
    normalized_image[i] = (float)resized_image[i] / 255.0;
  }
  int prediction = runModel(normalized_image);

  // Afficher la prédiction
  Serial.print("Prediction: ");
  Serial.println(prediction);

  // Attendre avant la prochaine capture d'image
  delay(1000);
}
