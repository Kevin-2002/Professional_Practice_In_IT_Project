#tutorial for Making flask tutorial
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
#note above is only used for the code layout and the install was just pip install flask in the cmd prompt

# IMPORTS #

#additional flask libraries explained
#render_template : for returning and rendering a html page
#request : used to extract files from the html form
#jsonify : used for error catching/handling
from flask import Flask, render_template, request, jsonify

#os used to get the current working directory the files are stored in and save files
import os

#Script that utilises the tesseract library and does the image recognition
import scripts.CharacterRecognition as CharacterRecognition

# FLASK APP #
app = Flask(__name__)

#config for saving files
app.config['UPLOAD_FOLDER'] = '../otherContent/storage'

@app.route('/')
def beginnerFlask():
    return render_template('HomePage.html')

#Useful link for declaring what type of listener method is being used
#https://pythonbasics.org/flask-http-methods/
@app.route('/RunCharacterRecognition', methods = ['POST'])
def runCharacterRecognition():
    #check that image is received
    if 'image' not in request.files:
        return jsonify({'error': 'No file'}), 400

    #extract the image from the form
    file = request.files['image']

    # Save the file to the upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Call ScanImageForText function to process the uploaded image
    detected_room = CharacterRecognition.ScanImageForText(file_path)

    if detected_room:
        return jsonify({'message': f'Room detected: {detected_room}'}), 200
    else:
        return jsonify({'message': 'Room not found in the image'}), 200

if __name__ == '__main__':
    app.debug = True#to restart the server as soon as changes are made
    app.run(host = '0.0.0.0', port = 3000)#runs localhost:3000