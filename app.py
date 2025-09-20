from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone
from flask_moment import Moment

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)

# Activity 1.3: Home page
@app.route('/')
def index():
    current_time = datetime.now(timezone.utc)
    return render_template('index.html', current_time=current_time)

# Example 3-6 (Errror Handlers)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

