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

from PIL import Image

def mkthumb(fp, h=128, w=128):
    """docstring for mkthumb"""

    size = (h, w)
    f, ext = os.path.splitext(fp)

    im = Image.open(fp)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('.thumbnail'.join([f, ext]))
