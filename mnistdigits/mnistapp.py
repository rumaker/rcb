from picamera import PiCamera
from time import sleep

camera = PiCamera(resolution=(1792,1792)) 
camera.start_preview()
sleep(10)
camera.capture('image.jpg')
camera.stop_preview()

from skimage.io import imread
import numpy as np

im = imread("image.jpg")

from skimage.transform import resize

# resize to 28 x 28
im_resize = resize(im,(28,28), mode='constant')

from skimage.color import rgb2gray

# turn the image from color to gray
im_gray = rgb2gray(im_resize)

# the color of the original set are inverted,so we invert it here
im_gray_invert = 255 - im_gray*255

#treat color under threshold as black
im_gray_invert[im_gray_invert<=90] = 0

from keras.models import load_model
model=load_model('mnist_trained_model.h5')
im_final = im_gray_invert.reshape(1,28,28,1)

# the below output is a array of possibility of respective digit
ans = model.predict(im_final)
print(ans)

# choose the digit with greatest possibility as predicted dight
ans = ans[0].tolist().index(max(ans[0].tolist()))
print("the predicted digit is",ans)

