from flask import Flask, render_template, flash


app = Flask(__name__)


# Create Login Page
@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/cars', methods=['GET', 'POST'])
def cars():
	return render_template('cars.html')

@app.route('/rolls', methods=['GET', 'POST'])
def rolls():
	return render_template('rolls.html')



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=5001)