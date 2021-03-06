# -*- coding: utf-8 -*-
"""ML WORKSHOP DAY 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qX9-IELLJsSLXm5ygl0v22YZyxq7y0CN
"""

import keras

from keras.datasets import mnist

data = mnist.load_data()

(train_images, train_labels),(test_images, test_labels) = data

len(train_images)

len(train_labels)

len(test_labels)

len(test_images)

train_images=train_images.reshape((60000, 28, 28, 1))

test_images=test_images.reshape((10000,28,28,1))

train_images[0]

train_images = train_images.astype('float')/255

test_images= test_images.astype('float')/255

from keras.preprocessing import image

import matplotlib.pyplot as plt

plt.imshow(image.array_to_img(train_images[77]), cmap='gray')

train_labels[77]

from keras.utils import to_categorical

train_labels_originals= train_labels

train_labels=to_categorical(train_labels)

train_labels_originals[1]

train_labels[1]

test_labels_originals=test_labels

test_labels=to_categorical(test_labels)

from keras import layers, models

model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape= (28,28,1)))

model.summary()

model.add(layers.MaxPooling2D((2,2)))

model.summary()

model.add(layers.Conv2D(64,(3,3), activation ='relu'))

model

model.summary()

model.add(layers.Flatten())

model.add(layers.Dense(64, activation='relu'))

model.summary()

model.add(layers.Dense(10,activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=10,batch_size= 64)

test_loss,test_accuracy = model.evaluate(test_images,test_labels)

test_accuracy

test_loss

predictions=model.predict(test_images)

plt.imshow(image.array_to_img(test_images[736]), cmap='gray')

