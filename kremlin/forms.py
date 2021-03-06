"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""

""" Module containing form classes and validation, for use with WTForms """

from flaskext.wtf import Form, TextField, TextAreaField, FileField, \
        BooleanField, PasswordField, file_allowed, file_required, validators

from kremlin import uploaded_images

class NewPostForm(Form):
    """ Post Form """
    name = TextField(u'Name', validators=[validators.required()])

    upload = FileField("Image File",
        validators=[
            file_required(),
            file_allowed(uploaded_images, "Not an image :("),
        ]
    )

    note = TextAreaField(u'Note/Comment', validators=[validators.optional()])

    tags = TextField(u'Tags (separated by space)',
            validators=[validators.optional()]
        )

class NewCommentForm(Form):
    """ Comment Form """
    name = TextField(u'Name', validators=[validators.required()])
    body = TextAreaField(u'Comment', validators=[validators.required()])

class LoginForm(Form):
    """ Login form for Kremlin application """
    username = TextField(u'Name', validators=[validators.required()])
    password = PasswordField(u'Password',
        validators=[validators.Required()]
    )

class RegisterForm(Form):
    """ Registration Form """
    username = TextField(u'Username',
        validators=[
            validators.Required(),
            validators.Length(min=3, max=25),
        ]
    )
    email = TextField(u'Email Address',
        validators=[
            validators.Required(),
            validators.Length(min=6, max=50),
            validators.Email(),
        ]
    )
    password = PasswordField(u'Password',
        validators = [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match!'),
        ]
    )
    confirm = PasswordField(u'Repeat Password')
    accept_tos = BooleanField(u'I accept the TOS',
        validators=[validators.Required()])
