import streamlit as st
from PIL import Image, UnidentifiedImageError
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import pyheif

# Title of the app
st.title("Image Format Converter")

# Supported image formats for upload
SUPPORTED_UPLOAD_FORMATS = [
    "jpeg", "jpg", "png", "bmp", "tiff", "tif", "webp", "pdf"
]

# Supported image formats for conversion
SUPPORTED_CONVERT_FORMATS = [
    "JPEG", "PNG", "BMP", "TIFF", "WEBP", "PDF"
]

# Default high quality option
DEFAULT_QUALITY = 95

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=SUPPORTED_UPLOAD_FORMATS)

if uploaded_file is not None:
    try:
        # Read image data from the uploaded file
        image_data = uploaded_file.read()

        # Handle HEIC file
        if uploaded_file.type == 'heic':
            heif_file = pyheif.read_heif(image_data)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
        else:
            # Use io.BytesIO to create a byte stream
            image_stream = io.BytesIO(image_data)
            # Open the image using PIL's Image.open()
            image = Image.open(image_stream)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Select the format to convert to
        format_to_convert = st.selectbox("Select format to convert to", SUPPORTED_CONVERT_FORMATS)

        if st.button("Convert"):
            # Convert the image
            converted_image = io.BytesIO()
            
            # Handle PDF conversion
            if format_to_convert == "PDF":
                # Save image to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    image.save(temp_file, format="JPEG")
                    temp_file_path = temp_file.name
                
                # Create a PDF canvas with A4 size
                c = canvas.Canvas(converted_image, pagesize=letter)
                width, height = letter

                # Adjust the image size and position
                img_width, img_height = image.size
                aspect_ratio = img_width / img_height

                # Fit image to page size while maintaining aspect ratio
                if img_width > img_height:
                    img_width = width
                    img_height = width / aspect_ratio
                else:
                    img_height = height
                    img_width = height * aspect_ratio
                
                x = (width - img_width) / 2
                y = (height - img_height) / 2

                c.drawImage(temp_file_path, x, y, img_width, img_height)
                c.showPage()
                c.save()
                mime = "application/pdf"
            else:
                # Set high quality option
                quality = DEFAULT_QUALITY
                image.save(converted_image, format=format_to_convert, quality=quality)
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
