from flask import Flask
from flask import render_template

#Coded and designed by Alan Espinoza

# creates a Flask application
app = Flask(__name__)
  
#Menu
@app.route("/")
def index():
    message = "Flask Media"
    return render_template('index.html', message=message)

#Ruta Imagen
@app.route("/image")
def serve_image():
    message = "Images:"
    return render_template('image.html', message=message)   

#Ruta Videos
@app.route("/video")
def serve_video():
    message = "Videos:"
    return render_template('video.html', message=message)

#Ruta Audios
@app.route("/audio")
def serve_audio():
    message = "Audios:"
    return render_template('audio.html', message=message)   

# run the application
if __name__ == "__main__":
    app.run(debug=True)

