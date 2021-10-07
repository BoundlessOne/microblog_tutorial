from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Boundless'}
    posts = [{'author': {'username': 'Chuang Tzu'},'body': 'The great clod burdens me with form.' },
        {'author': {'username': 'Lao Tzu'},'body' : 'These three I treasure: mercy, simplicity, humility.'}]
    return render_template('index.html', title='Wisdom Webbook', user=user, posts=posts)
