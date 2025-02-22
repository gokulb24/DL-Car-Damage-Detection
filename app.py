from PIL import Image
import streamlit as st
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)  # Convert BytesIO to an image
    st.image(image, caption="Uploaded File", use_container_width=True)

    image_path = "temp_file.jpg"
    image.save(image_path)  # Save the image properly

    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
