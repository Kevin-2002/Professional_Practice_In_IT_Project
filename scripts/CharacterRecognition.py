# Tutorials followed
# https://nanonets.com/blog/ocr-with-tesseract/ tesseract tutorial
# https://www.learndatasci.com/solutions/python-string-contains/#:~:text=The%20easiest%20and%20most%20effective,can't%20find%20the%20substring. regex subtring in python

# Import required packages
import pytesseract
import re

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

    #re.search() searches a variable with a regex expression
    if re.search("CR1|cr1", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604875&showpoidetails=true"

    elif re.search("CR2|cr2", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604863&showpoidetails=true"

    elif re.search("CR3|cr3", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604796&showpoidetails=true"

    elif re.search("CR4|cr4", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604795&showpoidetails=true"

    elif re.search("CR5|cr5|CRS", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010442,53.278791&zoom=18.6&sharepoitype=poi&sharepoi=1001604868&showpoidetails=true"

    elif re.search("CR6|cr6", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=1&center=-9.009998,53.278794&zoom=20.4&sharepoitype=poi&sharepoi=1001604718&showpoidetails=true"

    elif re.search("CR7|cr7", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604806&showpoidetails=true"

    elif re.search("CR8|cr8", textFromImage):
        detectedRoomLink = "https://use.mazemap.com/#v=1&campusid=954&zlevel=2&center=-9.010505,53.278868&zoom=18.8&sharepoitype=poi&sharepoi=1001604822&showpoidetails=true"

    else:
        detectedRoomLink = "Room not found!"

    return detectedRoomLink