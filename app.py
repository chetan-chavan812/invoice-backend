from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import re
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow React frontend to communicate
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/analyze', methods=['POST'])
def analyze_image():
    print("Request files:", request.files)  # debug print
    if 'image' not in request.files:
        return jsonify({"error": "No file received"}), 400

    file = request.files['image']
    filepath = os.path.join('uploads', file.filename)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')  # make folder if missing
    file.save(filepath)

    img = Image.open(filepath)
    text = pytesseract.image_to_string(img)

    date = re.findall(r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}", text)
    total = re.findall(r"(?:Total|Amount|Balance)\s*[:\-]?\s*\$?\s*(\d+\.\d{2})", text, re.IGNORECASE)
    gst = re.findall(r"(?:GST|Tax)\s*[:\-]?\s*\$?\s*(\d+\.\d{2})", text, re.IGNORECASE)
    rates = re.findall(r"\b\d+\.\d{2}\b", text)

    result = {
        "Date": date if date else "Not Found",
        "Total Amount": total if total else "Not Found",
        "GST": gst if gst else "Not Found",
        "Rates Found": rates if rates else "Not Found"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

