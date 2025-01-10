import streamlit as st
from rembg import remove
import numpy as np
import cv2
from io import BytesIO

def remove_background(input_image):
    # Use rembg to remove the background
    output_data = remove(input_image.read())
    
    # Convert the output data (bytes) into a numpy array
    output_image = np.frombuffer(output_data, np.uint8)
    
    # Decode the image
    output_image = cv2.imdecode(output_image, cv2.IMREAD_UNCHANGED)
    
    # Convert to PNG for transparent background
    _, output_png = cv2.imencode('.png', output_image)
    return output_png.tobytes()

def main():
    st.title("Background Removal from Image")
    st.write("Upload an image to remove its background")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Show the original image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Remove background
        output_image_bytes = remove_background(uploaded_file)

        # Show the background removed image
        st.image(output_image_bytes, caption="Background Removed Image", use_container_width=True)

        # Provide a download button
        st.download_button(
            label="Download Image with Background Removed",
            data=output_image_bytes,
            file_name="output.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
