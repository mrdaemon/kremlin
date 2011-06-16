"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import hashlib

from flask import request, session, render_template, flash, url_for, redirect
from werkzeug import secure_filename

from kremlin import app, db, dbmodel, forms

@app.route('/')
def home_index():
    """ Display the glasnost logo, attempt to replicate old behavior """
    return render_template('home.html')

@app.route('/images')
def entries_index():
    """ Show an index of image thumbnails """
    return render_template('board.html', form=forms.NewPostForm())

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """ Show post identified by post_id """
    post = dbmodel.Post.query.filter_by(id=post_id).get_or_404()
    # TODO: Write template for post views.
    return "Post view: %s" % (post)

@app.route('/add/', methods=['POST'])
def add_image():
    """ Add a new image """

    form = forms.NewPostForm()

    if form.validate_on_submit():
        filename = secure_filename(form.upload.file.filename)
        filedata = form.upload.stream.read()

        h = hashlib.new('sha1')
        h.update(filedata)
        filehash = h.hexdigest()

        # Validate file uniqueness
        dupe = dbmodel.Image.query.filter_by(sha1sum=filehash).first()

        if dupe:
            flash("Image already exists: %r" % (dupe))
            return redirect(url_for('entries_index'))
        else:
            # File is unique, proceed to create post and image.

            # Save file to filesystem
            try:
                forms.images.save(form.upload.file)
            except IOError:
                flash("Oh god a terrible error occured while saving %s" %
                    (filename))
            else:
                dbimage = dbmodel.Image(filename, filehash)
                db.session.add(dbimage)

                user = None

                if "uid" in session:
                    user = dbmodel.User.query.filter_by(
                            id=session['uid']
                        ).first()

                note = form.note

                #TODO: Implement tags.

                # Create a new post with the image
                post = dbmodel.Post(image=dbimage, title=filename,\
                        note=note, user=user)
                db.session.add(post)

                # Commit database transaction
                db.session.commit()
                flash("Image successfully posted!")

        return redirect(url_for('index'))





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


