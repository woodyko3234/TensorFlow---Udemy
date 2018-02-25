#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:26:21 2017

@author: justinwu
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (7,7) # Make the figures a bit bigger

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

nb_classes = 10

# the data, shuffled and split between tran and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print("X_train original shape", X_train.shape)
print("y_train original shape", y_train.shape)

import matplotlib.pyplot as plt
def plot_image(image,i):
    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    plt.imshow(image, cmap='binary')
    plt.title("Class {}".format(y_train[i]))
    plt.show()
    
plot_image(X_train[0],0)

for i in range(9):
    plot_image(X_train[i],i)
    
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print("Training matrix shape", X_train.shape)
print("Testing matrix shape", X_test.shape)

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu')) # An "activation" is just a non-linear function applied to the output
                              # of the layer above. Here, with a "rectified linear unit",
                              # we clamp all values below 0 to 0.
                           
model.add(Dropout(0.2))   # Dropout helps protect the model from memorizing or "overfitting" the training data
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

train_data=model.fit(X_train, Y_train,
          validation_split=0.2, epochs=8,
          batch_size=128, verbose=2)

import matplotlib.pyplot as plt
def show_train_figure(train_data,train,validation):
    plt.plot(train_data.history[train])
    plt.plot(train_data.history[validation])
    plt.title('Train data')
    plt.xlabel('Epoch')
    plt.ylabel('Acuracy')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()

show_train_figure(train_data,'acc','val_acc')
show_train_figure(train_data,'loss','val_loss')
score = model.evaluate(X_test, Y_test,)
print('Test score:', score[0])
print('Test accuracy:', score[1])
# The predict_classes function outputs the highest probability class
# according to the trained classifier for each input example.
predicted_classes = model.predict_classes(X_test)

# Check which items we got right / wrong
correct_indices = np.nonzero(predicted_classes == y_test)[0]
incorrect_indices = np.nonzero(predicted_classes != y_test)[0]
predicted_classes
def plot_figures_labels(figures,labels,prediction,idx,num=9):
    figure=plt.gcf()
    figure.set_size_inches(15,15)
    if num>16:
        num=16
    for i in range(0,num):
            ax=plt.subplot(3,3,i+1)
            ax.imshow(figures[idx].reshape(28,28),cmap='binary')
            title='label='+str(labels[idx])
            if len(prediction)>0:
                title+=",predict="+str(prediction[idx])
                
            ax.set_title(title,fontsize=12)
            ax.set_xticks([])
            ax.set_yticks([])
            idx+=1
    plt.show()

X_test[0]

plot_figures_labels(X_test,y_test,predicted_classes,idx=150,num=9)

incorrect_indices    
    