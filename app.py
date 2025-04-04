from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("def.html")
@app.route('/certificates')
def certificates():  # put application's code here
    return render_template("certificates.html")

@app.route('/logos')
def logos():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
