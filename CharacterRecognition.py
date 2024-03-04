# Tutorial followed
# https://nanonets.com/blog/ocr-with-tesseract/

# Import required packages
import cv2
import pytesseract

# Read in the image
img = cv2.imread('../OtherContent/Sample.jpg')

# Edit image here to help detection of characters

# Adding custom options
# --oem is a setting that does OCR Engine Configuration

# --psm is the way the searching for text in the image is conducting, 
# For example: --psm 6 is looking for a whole block of text
# Where as --psm 11 is looking for as much text as possible

# List of best options for me right now
# Custom_config = r'--oem 3 --psm 6'
custom_config = r'--oem 3 --psm 11'

# Do the image text-parsing
textFromImage = pytesseract.image_to_string(img, config=custom_config)

print(textFromImage)