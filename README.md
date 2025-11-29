🐱 Cat vs Dog Classifier App

A simple machine learning web application built with Streamlit and TensorFlow. This app allows users to upload an image and uses a pre-trained Deep Learning model to classify it as either a Cat or a Dog.

📋 Prerequisites

Before running the application, ensure you have the following installed:

Python (3.8 or higher recommended)

pip (Python package installer)

🛠️ Installation

Clone or Download this repository to your local machine.

Install the required Python libraries by running the following command in your terminal:

pip install streamlit tensorflow numpy pillow


⚙️ Setup

Important: The application requires a trained model file to function.

Ensure you have your trained Keras model file saved.

Rename your model file to model.keras (or update the filename in app.py to match your file).

Place model.keras in the same directory as app.py.

🚀 How to Run

Open your terminal or command prompt.

Navigate to the project directory.

Run the Streamlit app:

streamlit run app.py


The app should automatically open in your default web browser. If not, click the local URL provided in the terminal (usually http://localhost:8501).

📁 Project Structure

app.py: The main Streamlit application script.

model.keras: The pre-trained TensorFlow/Keras model (you must provide this).

README.md: This documentation file.

📝 Usage

Launch the app.

Click the "Browse files" button.

Select a JPG, JPEG, or PNG image of a cat or a dog.

The app will display the image and the predicted class ("Cat" or "Dog") along with a confidence score.
