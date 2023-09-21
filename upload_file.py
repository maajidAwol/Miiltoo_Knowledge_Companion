from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader
import os
import io

app = Flask(__name__)

# Define the folder where PDF files will be saved
UPLOAD_FOLDER = 'my_books'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        # Get the uploaded PDF file
        pdf_file = request.files['pdf_file']

        if pdf_file:
            # Get the name of the uploaded PDF file
            pdf_filename = pdf_file.filename

            # Create a path for the uploaded PDF file in the specified folder
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)

            # Save the PDF file to the specified folder
            pdf_file.save(pdf_path)

            # Read the PDF file
            pdf_reader = PdfReader(pdf_path)
            
            # Initialize a variable to store the text
            text = ""
            
            # Loop through each page and extract text
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Create a name for the output TXT file based on the PDF name
            txt_filename = os.path.splitext(pdf_filename)[0] + ".txt"
            
            # Create a path for the output TXT file in the specified folder
            txt_path = os.path.join(app.config['UPLOAD_FOLDER'], txt_filename)

            # Save the extracted text to a local TXT file
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)
            
            # Provide a download link for the TXT file
            return f"PDF to TXT conversion successful. <a href='/download/{txt_filename}'>Download TXT file</a>"

    return render_template('upload.html')

@app.route('/download/<filename>')
def download(filename):
    try:
        # Generate a file-like object for the TXT file
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb") as txt_file:
            file_data = io.BytesIO(txt_file.read())

        # Send the file as an attachment for download
        return send_file(
            file_data,
            as_attachment=True,
            download_name=filename,
            mimetype='text/plain'
        )

    except FileNotFoundError:
        return "File not found"

if __name__ == '__main__':
    # Ensure the "my_books" folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
