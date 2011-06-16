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
        file_allowed, file_required, validators

from kremlin import uploaded_images

class NewPostForm(Form):
    name = TextField(u'Name', validators=[validators.required()])

    upload = FileField("Image File",
                        validators=[file_required(),
                        file_allowed(uploaded_images, "Not an image :(")])

    note = TextAreaField(u'Note/Comment', validators=[validators.optional()])

    tags = TextField(u'Tags (separated by space)',
            validators=[validators.optional()]
        )


