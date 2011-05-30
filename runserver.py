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
import os
import sys

from kremlin import app

def usage():
    """ Display program usage """
    print """
    Kremlin startup helper program
    Mostly useful for development and testing purposes.
    -------------------------------
    usage: %s <configfile.cfg>

    Configuration file name or path is entirely optional, the default value of
    'kremlin.cfg' will be use should it be omitted. Useful for multiple
    configurations such as testing/development/production.

    You may also set the environment variable 'KREMLIN_CONFIGURATION' to
    obtain the same result, which also works when running the application by
    other means, such as fcgi, gunicorn or unsupported application servers.
    """ % (sys.argv[0])

def main():
    """ Program entry point when ran interactively """
    print "Kremlin Magical Everything System v 0.0.0-None"
    print "Copyright (c) Glasnost 2010-2011"
    print "-----------------------------------------------"

    # If no configuration is specified, use the default.
    if len(sys.argv) < 2:
        if not os.environ.has_key('KREMLIN_CONFIGURATION'):
            os.environ['KREMLIN_CONFIGURATION'] = \
                    os.path.abspath('kremlin.cfg')
    elif len(sys.argv) == 2:
        # TODO: Ugly as sin. In due time, add better argument parsing.
        if sys.argv[1].startswith('-'):
            usage()
            sys.exit(1)
        else:
            os.environ['KREMLIN_CONFIGURATION'] = sys.argv[1]
    else:
        usage()
        sys.exit(1)

    print "Connect to http://127.0.0.1:5000 to access."
    app.run(debug=True)

if __name__ == '__main__':
    main()
