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
    print "Launching kremlin in development mode."
    print "--------------------------------------"
    app.run(debug=True)

if __name__ == '__main__':
    main()
