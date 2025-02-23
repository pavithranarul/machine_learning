import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from crop_fertilizer_mapping import get_recommendations

# Load model
model = tf.keras.models.load_model("../models/soil_cnn_model.h5")
class_labels = ["alluvial", "black", "red", "clayey", "laterite", "sandy"]

def predict_soil(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    soil_type = class_labels[np.argmax(prediction)]
    
    crops, fertilizers = get_recommendations(soil_type)
    
    return soil_type, crops, fertilizers

