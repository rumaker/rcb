import os
import glob
import argparse

import numpy as np
import tensorflow as tf
# Used tensorflow Keras to get easy Flatten command
from tensorflow import keras
from skimage import color, io, img_as_uint, img_as_float, transform

parser=argparse.ArgumentParser(description = 'Get image diretory to identify number from')
parser.add_argument('directories', nargs="+", help='list of directories to identify image data')
args=parser.parse_args()
args.directories.sort()
print(args)

print("1. imports complete") 
model = keras.models.Sequential()  # a basic feed-forward model

# Keras Flatten needs an input shape tf.keras doesn't need input_shape
# Changed example to tf.keras
# model.add(keras.layers.Flatten())# takes our 28x28 and makes it 1x784
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10,activation=tf.nn.softmax))

print("2. keras model set up complete") 
# step 4 // compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("3. keras model compiled") 
print(model.summary())
# load weights into model

model.load_weights('epic_num_reader.h5')

print("4. keras model weights loaded") 
print("For testing we need to load the test data")


#imgfile = os.path.join("./testimgs", args.filename)
#img = io.imread(imgfile)
#
#step 9 // predict
for directory in args.directories:
    imgfiles = glob.glob(os.path.join(directory, '*.png'))
    for imgfile in sorted(imgfiles):
        img = io.imread(imgfile)
        predictions = model.predict(np.expand_dims(img,axis=0))
        print(np.argmax(predictions, axis=1) , ": ", imgfile)


