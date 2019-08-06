import cyni
import numpy as np
from PIL import Image
import time

class SimpleCapture:
    """docstring for SimpleCapture
    Simple class to capture frames of depthmap and ir images
    """
    def __init__(self):
        pass
        
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

    def get_next_frame_clean(self, save=1):
        self.depthStream.start()
        self.depthFrame = self.depthStream.readFrame()
        self.depthStream.stop()
        self.irFrame = self.irStream.readFrame()

        # colorFrame = colorStream.readFrame()
    
        # TODO : Review depthMapToImage in the code below
        # TODO : Does the function depthMapToImage apply to irFrame as well????

        depthImage = None
        depthImage = Image.fromarray(cyni.depthMapToImage(self.depthFrame.data))
        

        irImage = Image.fromarray(cyni.depthMapToImage(self.irFrame.data))
        #colorImage = Image.fromarray(colorFrame.data)

        if (save==1):
            timestamp = time.time()
            irImage_filename = "ir" +  str(timestamp)+".png"
            depthImage_filename = "depth" +  str(timestamp)+".png"
            depthImage.save("/home/madhav/Desktop/Structure-Sensor/Work/Robotic-Vision/cythonNI/examples/capture/depth"+str(timestamp)+".png")
            #colorImage.save("capture/color"+str(timestamp)+".png")
            irImage.save("/home/madhav/Desktop/Structure-Sensor/Work/Robotic-Vision/cythonNI/examples/capture/ir"+str(timestamp)+".png")

        return depthImage, irImage, irImage_filename, depthImage_filename #, colorImage

    def get_next_frame(self, save=1):
        self.depthFrame = self.depthStream.readFrame()
        self.irFrame = self.irStream.readFrame()
        # colorFrame = colorStream.readFrame()
    
        # TODO : Review depthMapToImage in the code below
        # TODO : Does the function depthMapToImage apply to irFrame as well????

        depthImage = Image.fromarray(cyni.depthMapToImage(self.depthFrame.data))
        irImage = Image.fromarray(cyni.depthMapToImage(self.irFrame.data))
        #colorImage = Image.fromarray(colorFrame.data)

        if (save==1):
            timestamp = time.time()
            irImage_filename = "ir" +  str(timestamp)+".png"
            depthImage_filename = "depth" + str(timestamp)+".png" 
            depthImage.save("/home/madhav/Desktop/Structure-Sensor/Work/Robotic-Vision/cythonNI/examples/capture/depth"+str(timestamp)+".png")
            #colorImage.save("capture/color"+str(timestamp)+".png")
            irImage.save("/home/madhav/Desktop/Structure-Sensor/Work/Robotic-Vision/cythonNI/examples/capture/ir"+str(timestamp)+".png")

        return depthImage, irImage, irImage_filename, depthImage_filename #, colorImage
    
    def end_capture(self):
        self.device.close()

if __name__ == "__main__":
    depth_capture = SimpleCapture()
    depth_capture.setup_cature()
    # while 1:
    depthImg, irImg, irImage_filename, depthImage_filename = depth_capture.get_next_frame_clean()
    print irImage_filename
    depth_capture.end_capture()