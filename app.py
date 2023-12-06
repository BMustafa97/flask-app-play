from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
