from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from babel.dates import format_datetime

app = Flask(__name__)
Bootstrap(app)

# Activity 1.3: Home page
@app.route('/')
def index():
    # Get current datetime
    now = datetime.now()
    # Babel uses "full" instead of "LLLL"
    timestamp = format_datetime(now, format='full', locale='en_US')
    return render_template('index.html', name="Kylie", timestamp=timestamp)

# User page (from Example 2-2, 3-3, but fixed)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Example 3-6 (Errror Handlers)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

