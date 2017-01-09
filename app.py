from flask import Flask, render_template, request, session, redirect, url_for
#from flask_bootstrap import Bootstrap


app = Flask(__name__)
#Bootstrap(app)

#app.secret_key = os.urandom(10)


@app.route("/")
def main():
    return render_template('login.html')



if(__name__ == "__main__"):
	app.debug = True
	app.run();
