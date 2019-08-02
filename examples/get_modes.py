import cyni
import numpy as np
from PIL import Image

cyni.initialize()
device = cyni.getAnyDevice()
device.open()
print "Depth:"
print device.getSupportedVideoModes("depth")

print "ir:"
print device.getSupportedVideoModes("ir")

# print "Color:"
# print device.getSupportedVideoModes("color")

device.close()