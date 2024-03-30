# Tutorials followed
# https://nanonets.com/blog/ocr-with-tesseract/ tesseract tutorial
# https://www.learndatasci.com/solutions/python-string-contains/#:~:text=The%20easiest%20and%20most%20effective,can't%20find%20the%20substring. regex subtring in python


# Import required packages
import cv2
import pytesseract
import re

# Read in the image
#img = cv2.imread('../OtherContent/Sample.jpg')
img = cv2.imread('../OtherContent/SampleCr4.png')

#function for text detection
def ScanImageForText(img):
    # Adding custom options in our search of the image
    # --oem is a setting that does OCR Engine Configuration
    # for example --oem 3 uses whichever engine is available

    # --psm changes the way the searching for text in the image is conducted, 
    # For example: --psm 6 is looking for a whole block of text
    # Where as --psm 11 is looking for as much text as possible wherever it can find it

    # List of best options for me right now
    custom_config = r'--oem 3 --psm 6'
    # custom_config = r'--oem 3 --psm 11'

    # Do the image text-parsing
    textFromImage = pytesseract.image_to_string(img, config=custom_config)

    print(textFromImage)

    if re.search("CR1|cr1", textFromImage):
        detectedRoom = "CR1"

    elif re.search("CR2|cr2", textFromImage):
        detectedRoom = "CR2"

    elif re.search("CR3|cr3", textFromImage):
        detectedRoom = "CR3"

    elif re.search("CR4|cr4", textFromImage):
        detectedRoom = "CR4"

    elif re.search("CR5|cr5|CRS", textFromImage):
        detectedRoom = "CR5"

    elif re.search("CR6|cr6", textFromImage):
        detectedRoom = "CR6"

    elif re.search("CR7|cr7", textFromImage):
        detectedRoom = "CR7"

    elif re.search("CR8|cr8", textFromImage):
        detectedRoom = "CR8"

    else:
        detectedRoom = "Room not found!"

    return detectedRoom