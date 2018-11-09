import numpy as np
import tensorflow as tf
# Used tensorflow Keras to get easy Flatten command
from tensorflow import keras

import os
from skimage import color, io, img_as_uint, img_as_float, transform


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

fn = "iosave2018-11-08T16:40:31.191327.png"
imgfile = os.path.join("./testimgs", fn)

img = io.imread(imgfile)
x_test = img

#mnist = keras.datasets.mnist #28x28 images of handwritte digits 0-9
##step 1
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

##step 2 // normalize the inputs
#x_train = keras.utils.normalize(x_train, axis=1)
#x_test = keras.utils.normalize(x_test, axis=1)

#xtest =
#ytest = 

#step 9 // predict
predictions = model.predict(np.expand_dims(x_test,axis=0))



print("5. keras model prediction results") 
print(np.argmax(predictions, axis=1))
#print(y_test)

#index=100
#print(np.argmax(predictions[index]))


