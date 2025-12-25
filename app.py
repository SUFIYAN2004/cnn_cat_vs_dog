import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.models import load_model
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐾",
    layout="centered"
)

# --- Title and Description ---
st.title("🐱 Cat vs Dog Classifier 🐶")
st.write("Upload an image to check if it's a **Cat** or a **Dog**!")

# --- Model Loading ---
# We use @st.cache_resource to load the model only once to save time
@st.cache_resource
def load_classifier_model():
    try:
        # REPLACE 'model.keras' WITH YOUR ACTUAL MODEL PATH
        model_path = 'Model.h5' 
        model = load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.warning("Please make sure your model file (e.g., 'model.keras') is in the same directory.")
        return None

model = load_classifier_model()

# --- Image Upload ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and model is not None:
    # 1. Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image',use_container_width=True)
    
    st.write("Classifying...")

    # 2. Preprocessing (Matching your logic)
    # We use PIL to open the file directly from the uploader
    img = Image.open(uploaded_file)
    
    # Resize to the target size expected by the model (64x64)
    img = img.resize((64, 64))
    
    # Convert to array
    img_array = keras_image.img_to_array(img)
    
    # Expand dims (axis=0) to create a batch of 1
    img_array = np.expand_dims(img_array, axis=0)

    # Note: If your training used rescale=1./255, uncomment the line below:
    # img_array = img_array / 255.0

    # 3. Prediction
    result = model.predict(img_array)
    
    # 4. Result Logic
    # Assuming binary classification where 1 is Dog and 0 is Cat
    # We use > 0.5 for stability, but this matches your logic of checking for 1
    prediction = ""
    probability = result[0][0]

    if probability > 0.5:
        prediction = 'Dog 🐶'
    else:
        prediction = 'Cat 🐱'

    # --- Display Result ---
    st.success(f"Prediction: **{prediction}**")

elif model is None:

    st.error("Model not loaded. Please ensure 'model.keras' exists.")
