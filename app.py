from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        url = request.form['url']
        # check if the url is valid
        if url:
            # check it starts with http:// or https://
            if url.startswith('http://') or url.startswith('https://'):
                print(url)
                return render_template('home.html', url=url)
            else:
                url = 'https://' + url
                print(url)
                return render_template('home.html', url=url)

        return render_template('home.html')
    return render_template('test.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
