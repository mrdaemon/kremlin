#!/usr/bin/python
"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
from __future__ import with_statement # python <2.7 support
from datetime import datetime
import hashlib

from flaskext.sqlalchemy import SQLAlchemy

from kremlin import app

# FIXME: temporary, for dev purposes. Move me to __init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)


# Tags helper table
# Since this is a many to many relationship, I'm using an actual table
# instead of a dynamic model. It is much more efficient in that
# scenario.
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

class User(db.Model):
    """ Declarative class for Users database table """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    """ Declarative class for Posts database table """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    note = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    # Foreign key for image attached to post
    # :relationaldatabases:
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    image = db.relationship('Image',
        backref=db.backref('images', lazy='dynamic'))

    def __init__(self, image, title=None, note=None, pub_date=None):
        self.image = image
        self.title = title
        self.note = note
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Post %r>' % self.title

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sha1sum = db.Column(db.String(40), unique=True) # 40 bytes SHA1

    # FIXME: Consider moving SHA hash computation to controller.
    # It is really, really out of place here I just thought it was nice
    # to autogenerate it like the date field, but then again, I'm not
    # sure if this is just going to be the declarative ORM stuff, or  a
    # full fledged MVC model. Whatever seems more pythonic to me later
    # on. Also, passing the file data around seems awkward.

    def __init__(self, name, filedata):
        self.name = name

        h = hashlib.new('sha1')
        h.update(filedata)
        self.sha1sum = h.hexdigest()

    def __repr__(self):
        return '<Image with checksum %r>' % self.sha1sum

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    # Foreign key relationship for users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('users', lazy='dynamic'))

    # Foreign key for parent post
    parent_post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    parent_post = db.relationship('Post',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, user, parent_post, body, pub_date=None):
        self.user = user
        self.parent_post = parent_post
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Comment by %r>' % self.user
