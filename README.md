# Image Format Converter

This Streamlit app allows users to upload an image, convert it to a different format, and download the converted image. It supports a wide range of image formats for both upload and conversion.
![p_converter](https://github.com/user-attachments/assets/ef1a31e5-e60b-43b3-be29-9dc52a29bc75)

## Features

- **Supported Upload Formats:** `jpeg`, `jpg`, `png`, `bmp`, `tiff`, `tif`, `webp`, `pdf`
- **Supported Conversion Formats:** `JPEG`, `PNG`, `BMP`, `TIFF`, `WEBP`, `PDF`
- **High-Quality Conversion:** Default conversion quality is set to 95%
- **HEIC File Handling:** Converts HEIC images for compatibility
- **PDF Conversion:** Converts images to PDF format, automatically adjusting size to fit an A4 page while maintaining the aspect ratio.

## How to Use

- **Upload an Image:** Click on "Upload an image" and select an image file in any of the supported formats.
- **Preview the Image:** The uploaded image is displayed on the page.
- **Choose Format for Conversion:** Use the dropdown to select the desired output format.
- **Convert and Download:** Press the "Convert" button. Once converted, a download link is provided for the new file.

## Demo
Check out the deployed app: [Image Converter ](https://your-streamlit-app-link](https://imageextentionconverter-saketh07.streamlit.app/)
## Installation Guide

Follow these steps to install and set up the Image Format Converter app.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/image-format-converter.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd image-format-converter
   ```

3. **Set Up a Virtual Environment (Recommended):**
   - **Create the virtual environment:**
     ```bash
     python -m venv venv
     ```
   - **Activate the virtual environment:**
     - **On Windows:**
       ```bash
       .\venv\Scripts\activate
       ```
     - **On macOS and Linux:**
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of the main Python file containing the Streamlit app.

6. **Access the Application:**

   Open the provided local URL (usually `http://localhost:8501`) in your web browser to start using the app.


