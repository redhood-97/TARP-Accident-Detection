# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:30:47 2018

@author: Abhilash Srivastava
"""
import numpy as np
from keras.datasets import cifar10
import matplotlib.pyplot as plt
from scipy.misc import toimage
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.utils import np_utils
from keras.models import model_from_json
import os
import cv2
np.random.seed(7)
epochs=25
lrate=0.01
decay=lrate/epochs
sgd=SGD(lr=lrate,momentum=0.9,decay=decay,nesterov=False)
template='C:\\Users\\Abhilash Srivastava\\Desktop\\study materials\\two-way_traffic-monitoring\\two-way_traffic-monitoring\\two_way_traffic\\img\\'
#loading the data
(x_train,y_train),(x_test,y_test)=cifar10.load_data()
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train=x_train/255.0
x_test=x_test/255.0

y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)
num_classes=y_test.shape[1]
'''
for i in range(0,9):
    plt.subplot(330 +1+i)
    plt.imshow(toimage(x_train[i]))
plt.show()
'''
#setting up the network
model=Sequential()
model.add(Conv2D(32,(3,3),input_shape=(32,32,3),padding='same',activation='relu',kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Conv2D(32,(3,3),padding='same',activation='relu',kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(512,activation='relu',kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation='softmax'))

json_file=open('model.json','r')
loaded_model_json=json_file.read()
json_file.close()
loaded_model=model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model.h5")
print("loaded model from disk")
loaded_model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
template='C:\\Users\\Abhilash Srivastava\\Desktop\\study materials\\two-way_traffic-monitoring\\two-way_traffic-monitoring\\two_way_traffic\\img\\'
file=template+'traffic1.jpg'
img=cv2.imread(file)
r=32.0/img.shape[1]
dim=(32,int(img.shape[0]*r))
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
#cv2.imshow("resized",resized)
#cv2.waitKey(0)
predict=loaded_model.predict(resized,batch_size=None,verbose=0)
