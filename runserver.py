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

from kremlin import app

def main():
    print "Kremlin Magical Everything System v 0.0.0-None"
    print "Copyright (c) Glasnost 2010-2011"
    print "-----------------------------------------------"
    print "RUNNING IN DEVELOPMENT MODE! ** NOT FOR PRODUCTION **"
    print "Connect to http://127.0.0.1:5000 to access."
    app.run(debug=True)

if __name__ == '__main__':
    main()
