import streamlit as st
from PIL import Image, UnidentifiedImageError
import io
from reportlab.pdfgen import canvas

# Title of the app
st.title("JPG to PDF Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a JPG image", type=["jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Read image data from the uploaded file
        image_data = uploaded_file.read()
        
        # Open the image using PIL's Image.open()
        image = Image.open(io.BytesIO(image_data))
        
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Convert to PDF"):
            # Convert the image to PDF
            pdf_bytes = io.BytesIO()
            c = canvas.Canvas(pdf_bytes)
            c.setPageSize((image.width, image.height))
            c.drawImage(io.BytesIO(image_data), 0, 0)
            c.showPage()
            c.save()
            
            # Provide download link
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name="converted_image.pdf",
                mime="application/pdf"
            )
    except UnidentifiedImageError:
        st.error("The uploaded file is not a valid image or is not supported. Please upload a valid JPG image file.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
