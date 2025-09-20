from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)
moment = Moment(app)

# Form class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

    # Custom validator to check UofT email
    def validate_email(self, field):
        if 'utoronto' not in field.data.lower():
            raise ValidationError('Please enter a valid UofT email address.')

# Activity 1.3: Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        # Save name and email in session
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    
    # Get current time in utc timezone in LLLL format
    current_time = datetime.now(timezone.utc)

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        email=session.get('email'),
        current_time=current_time
    )

# Example 3-6 (Errror Handlers)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500