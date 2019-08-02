import cyni
import numpy as np
from PIL import Image
import time

class SimpleCapture(object):
    """docstring for SimpleCapture
    Simple class to capture frames of depthmap and ir images
    """
    def __init__(self, arg=None):
        super(SimpleCapture, self).__init__()
        self.arg = arg
        
    def setup_cature(self):
        cyni.initialize()
        self.device = cyni.getAnyDevice()
        self.device.open()

        self.depthStream = self.device.createStream("depth", fps=30, width=640, height=480)
        self.irStream = self.device.createStream("ir", fps=30, width=640, height=480)
        # colorStream = device.createStream("color", fps=30)

        self.depthStream.start()
        self.irStream.start()
        # colorStream.start()

    def get_next_frame(self, save=0):
        self.depthFrame = self.depthStream.readFrame()
        self.irFrame = self.irStream.readFrame()
        # colorFrame = colorStream.readFrame()
        print (max(self.irFrame.data.tolist()))

        depthImage = Image.fromarray(cyni.depthMapToImage(self.depthFrame.data))
        irImage = Image.fromarray(cyni.depthMapToImage(self.irFrame.data))
        #colorImage = Image.fromarray(colorFrame.data)
        
        if (save==1):
            
            depthImage.save("capture/depth"+str(timestamp)+".png")
            #colorImage.save("capture/color"+str(timestamp)+".png")
            irImage.save("capture/ir"+str(timestamp)+".png")

        return depthImage, irImage #colorImage
    
    def end_capture(self):
        self.device.close()