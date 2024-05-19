import streamlit as st
from PIL import Image
import io

# Title of the app
st.title("Image Format Converter")

# Supported image formats
SUPPORTED_FORMATS = [
    "JPEG", "PNG", "BMP", "GIF", "TIFF", "WEBP", "ICO", "PDF", 
    "EPS", "SVG", "PSD", "HEIC", "HDR", "EXR", "TGA", "WMF", 
    "EMF", "J2K", "PCX", "PCT"
]

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=[f.lower() for f in SUPPORTED_FORMATS])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Select the format to convert to
    format_to_convert = st.selectbox("Select format to convert to", SUPPORTED_FORMATS)

    if st.button("Convert"):
        # Convert the image
        converted_image = io.BytesIO()
        # Special handling for formats that are not natively supported by PIL
        if format_to_convert in ["EPS", "SVG", "PSD", "HEIC", "HDR", "EXR", "TGA", "WMF", "EMF", "J2K", "PCX", "PCT"]:
            st.error(f"Conversion to {format_to_convert} is not supported by PIL. Please choose another format.")
        else:
            image.save(converted_image, format=format_to_convert)
            converted_image.seek(0)
        
            # Provide download link
            st.download_button(
                label="Download Converted Image",
                data=converted_image,
                file_name=f"converted_image.{format_to_convert.lower()}",
                mime=f"image/{format_to_convert.lower() if format_to_convert.lower() != 'pdf' else 'application/pdf'}"
            )
