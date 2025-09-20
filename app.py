from flask import Flask, render_template
app = Flask(__name__)

# Example 2-1
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Example 2-2
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# Example 3-3
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name-name)

# Example 3-6
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

