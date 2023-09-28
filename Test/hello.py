from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cv', methods=['GET', 'POST'])
def cv():
    return render_template("cv.html")


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return "Hello World Youness!"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
