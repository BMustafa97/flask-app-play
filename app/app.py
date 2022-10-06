from flask import Flask, render_template, flash
from flask_wtf import FlaskForm


app = Flask(__name__)


# Create Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template('index.html', form=form)




if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=5000)