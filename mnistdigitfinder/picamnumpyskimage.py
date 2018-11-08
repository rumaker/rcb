from picamera import PiCamera
from gpiozero import Button, LED
from datetime import datetime
from signal import pause

from skimage import color, io, img_as_uint, img_as_float, transform
import numpy as np

led = LED(17)
button = Button(2)

#Deprecated in favor of default imageio plugin
#io.use_plugin('freeimage')


cam = PiCamera()
cam.resolution = (256, 256)
cam.framerate = 30

def capture():
    led.on()
    dt =datetime.now().isoformat()
    image  = np.empty((256, 256, 3), dtype=np.uint8)
    cam.capture(image,'rgb')
    image = color.rgb2gray(image)
    image = transform.resize(image, (28, 28))
    #image = img_as_uint(image)
    io.imsave('/home/pi/Pictures/iosave%s.png' % dt , image)
    led.off()

print("Cam Setup")
led.on()
button.when_pressed = capture
print("Button Ready: Take Photos")
led.off()
pause()
cam.close()


