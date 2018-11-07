from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause

led = LED(17)
button = Button(2)
camera = PiCamera()

def capture():
  led.on()
  dt = datetime.now().isoformat()
  camera.capture('/home/pi/%s.jpg' % dt)
  led.off()

button.when_pressed = capture
pause()

