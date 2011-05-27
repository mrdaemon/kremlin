"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""

from flask import request, session, render_template, flash

from kremlin import app

@app.route('/')
def home_index():
    """ Display the glasnost logo, attempt to replicate old behavior """
    return render_template('home.html')

@app.route('/images')
def entries_index():
    """ Show an index of image thumbnails """
    return render_template('board.html')

@app.route('/post/<int:post_id>')
def post_id(post_id):
    """ Show post identified by post_id """
    return "Post view: %s" % (post_id)

@app.route('/add', methods=['POST'])
def add_image():
    """ Add a new image """
    return "Add a new image"

@app.route('/login', methods=['GET','POST'])
def login():
    """ Login to imageboard """
    error = None
    if request.method == 'POST':
        #TODO: Validate username
        pass
    return "Log in"

@app.route('/logout')
def logout():
    """ Logout of imageboard """
    session.pop('logged_in', None)
    flash('Logged out of Kremlin.')
    return "You have been logged out."

@app.route('/register')
def register():
    return "Unimplemented stub because fuck you, that's why."

@app.route('/about')
def about():
    return "Kremlin Everything System and Boredom Inhibitor v 0.0.0-None"


