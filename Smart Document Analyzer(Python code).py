import os
from PIL import Image
import pytesseract
import re

# Connect Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#  Folder containing all images
folder_path = r"C:\Users\Admin\Desktop\project"

#  Valid image formats
valid_extensions = ('.png', '.jpg', '.jpeg')

#  Loop through each image in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(valid_extensions):
        image_path = os.path.join(folder_path, filename)

        print("\n" + "=" * 50)
        print(f"🧾 Analyzing: {filename}")
        print("=" * 50)

        try:
            # Open image
            img = Image.open(image_path)

            # Read text from image
            text = pytesseract.image_to_string(img)
            print("Text found in image:")
            print(text)

            # Find date (like 12/05/2024 or 12-05-2024)
            date = re.findall(r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}", text)

            # Find total amount
            total = re.findall(r"(?:Total|Amount|Balance)\s*[:\-]?\s*\$?\s*(\d+\.\d{2})", text, re.IGNORECASE)

            # Show analyzed data
            print("\n===============================")
            print("Important Info from Document:")
            print("===============================")
            print("Date:", date if date else "Not Found")
            print("Total Amount:", total if total else "Not Found")

        except Exception as e:
            print(f"⚠️ Error analyzing {filename}: {e}")

print("\n Analysis complete for all images.")
