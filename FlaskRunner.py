#tutorial for Making flask tutorial
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
#note above is only used for the code layout and the install was just pip install flask in the cmd prompt

from flask import Flask
app = Flask(__name__)

@app.route('/')
def beginnerFlask():
    return "working"

if __name__ == '__main__':
    app.debug = True#to restart the server as soon as changes are made
    app.run(host = '0.0.0.0', port = 3000)#runs localhost:3000