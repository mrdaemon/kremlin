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

from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

from kremlin import app

@app.route('/')
def entries_index():
    """ Show an index of image thumbnails """
    return "Image index."

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


