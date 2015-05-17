from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Wassup!'

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/business')
def business():
    """Renders the business page."""
    return render_template(
        'business.html',
        title='ReUse Business - Add or Edit',
        year=datetime.now().year,
    )

@app.route('/new')
def new():
    """Renders the new page."""
    return render_template(
        'new.html',
        title='New Item Or Category',
        year=datetime.now().year,
    )

@app.route('/edit')
def edit():
    """Renders the edit page."""
    return render_template(
        'edit.html',
        title='Edit Item or Category',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact info goes here.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='ReUse business information goes here.'
    )

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Hey.  What are you doing here.', 404
