#!/usr/bin/env python
"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import sys

from yaml import load

# Attempt to use the libyaml C loader, fallback to pure python
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from kremlin import app

configdata = None

def readconfigdata(profile="development"):
    try:
        configdata = load(file('configuration.yml').read(), Loader=Loader)
    except IOError:
        print "Unable to read 'configuration.yml'!"
        print "Ensure it is present in the current directory and try again."
        sys.exit(1)

    if configdata.has_key(profile):
        print "Loading configuration data for %s..." % (profile)
        config = configdata[profile]

        internal_values = ['DEBUG','TESTING','SECRET_KEY',]

def main():
    print "Kremlin Magical Everything System v 0.0.0-None"
    print "Copyright (c) Glasnost 2010-2011"
    print "-----------------------------------------------"
    app.run(debug=True)

if __name__ == '__main__':
    main()
