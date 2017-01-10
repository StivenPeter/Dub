from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.utils import secure_filename

#from flask_bootstrap import Bootstrap
#from utils import

#Bootstrap(app)
#app.secret_key = os.urandom(10)
UPLOAD_FOLDER="static"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file(f):
    file = f['upload']
    filename = "default.jpg"
    if file.filename == '':
        return render_template("error.html")
    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except IOError:
        return render_template("error.html")
    return filename


@app.route("/")
@app.route("/home/")
def main():
    return render_template('login.html')


@app.route("/about/")
def about():
    return render_template("about.html") 



if(__name__ == "__main__"):
	app.debug = True
	app.run();
