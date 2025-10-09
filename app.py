# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hola")
def HOLA():
    return "Hola!"

@app.route("/user/<string:username>",methods=['GET'])
def show_user_name(username):
    print('type(username):',type(username))
    return 'String => {}'.format(username)

@app.route("/user/<int:id>",methods=['GET'])
def show_user_id(id):
    print('type(id): ',type(id))
    return 'int => {}'.format(id)

@app.route("/user/<float:version>",methods=['GET'])
def show_user_version(version):
    print('type(version): ',type(version))
    return 'float => {}'.format(version)

@app.route("/user/test")
def test():
    return '<html><body><h1>Test</h1></body></html>'

vars= 'Ruuu_vars'
@app.route("/user/home")
def home():
    return render_template("home.html", text=vars)

@app.route("/user/appinfo")
def appinfo():
    appinfo = {
        'app_id': '314',
        'app_name': 'Flask'
    }
    return render_template("home.html", AppInfo=appinfo)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)