from flask import Flask

app = Flask(__name__)

@app.route('/kontakt/', methods=['GET', 'POST'])
def kontakt():
    return "Ring Youness!"

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return "Hello World Youness!"

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Välkommen till Youness!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)