from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hem/', methods=['GET', 'POST'])
def hem():
    return render_template("index.html")

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return "Hello World Youness!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)            