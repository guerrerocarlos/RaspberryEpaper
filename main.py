import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in7b
from PIL import Image
import time

epd = epd2in7b.EPD()
epd.init()
epd.Clear()
time.sleep(1)

HBlackimage = Image.open(os.path.join(picdir, '2in7_Scale.bmp'))
HRedimage = Image.open(os.path.join(picdir, '2in7b-r.bmp'))
epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
time.sleep(2)

epd.sleep()
