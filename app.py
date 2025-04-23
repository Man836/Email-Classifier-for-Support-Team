import gradio as gr
from utils import mask_pii  # Ensure this function is defined in utils.py
import joblib
import json

# Load model
model = joblib.load("model/classifier.pkl")  # Adjust the path as necessary

# Function to classify email
def classify_email(email_body: str):
    # Mask PII and get entities
    masked_email, entities = mask_pii(email_body)
    
    # Predict the category using the loaded model
    category = model.predict([masked_email])[0]
    
    # Prepare the response in the required format
    response = {
        "input_email_body": email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
    
    return response

# Gradio interface
iface = gr.Interface(
    fn=classify_email,
    inputs="text",
    outputs="json",
    title="Email Classifier with PII Masking",
    description="Enter an email body to classify it and mask any personally identifiable information (PII)."
)

# Run the interface
if __name__ == "__main__":
    iface.launch(share=True)  # Set share=True to get a public link