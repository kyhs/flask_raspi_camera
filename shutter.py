from flask import Flask, request, send_file
import time
import picamera
from datetime import datetime

app = Flask(__name__)

@app.route('/shutter')
def shutter():
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        camera.capture(date+'.jpg')
    filename = date+'.jpg'
    try:
        return send_file(filename, attachment_filename='test.jpg')
    except:
        return "false1"
    return "false2"

@app.route('/test')
def sample():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
