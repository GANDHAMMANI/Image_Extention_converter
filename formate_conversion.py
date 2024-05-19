import streamlit as st
from PIL import Image, UnidentifiedImageError
import pillow_heif
import io
from reportlab.pdfgen import canvas

# Register HEIF plugin
pillow_heif.register_heif_opener()

# Title of the app
st.title("Image Format Converter")

# Supported image formats for upload
SUPPORTED_UPLOAD_FORMATS = [
    "jpeg", "jpg", "png", "bmp", "gif", "tiff", "tif", "webp", "ico", "pdf",
    "eps", "svg", "psd", "heic", "hdr", "exr", "tga", "wmf", "emf", 
    "j2k", "pcx", "pct"
]

# Supported image formats for conversion
SUPPORTED_CONVERT_FORMATS = [
    "JPEG", "PNG", "BMP", "GIF", "TIFF", "WEBP", "ICO", "PDF",
    "EPS", "SVG", "PSD", "HEIC", "HDR", "EXR", "TGA", "WMF", 
    "EMF", "J2K", "PCX", "PCT"
]

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=SUPPORTED_UPLOAD_FORMATS)

if uploaded_file is not None:
    try:
        # Attempt to open the uploaded file as an image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Select the format to convert to
        format_to_convert = st.selectbox("Select format to convert to", SUPPORTED_CONVERT_FORMATS)

        if st.button("Convert"):
            # Convert the image
            converted_image = io.BytesIO()
            
            # Handle PDF conversion
            if format_to_convert == "PDF":
                c = canvas.Canvas(converted_image)
                c.drawImage(uploaded_file, 0, 0)
                c.save()
                mime = "application/pdf"
            else:
                image.save(converted_image, format=format_to_convert)
                mime = f"image/{format_to_convert.lower()}"
            
            converted_image.seek(0)
            
            # Provide download link
            st.download_button(
                label="Download Converted Image",
                data=converted_image,
                file_name=f"converted_image.{format_to_convert.lower()}",
                mime=mime
            )
    except UnidentifiedImageError:
        st.error("The uploaded file is not a valid image or is not supported. Please upload a valid image file.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
