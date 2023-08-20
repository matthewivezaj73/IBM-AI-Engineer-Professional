#Importing libraries
import keras
from keras.models import Sequential 
from keras.layers import Dense
from keras.utils import to_categorical
#Creating a sequential model.
model = Sequential()
#Specifying the number of columns.
n_cols = car_data.shape[1]
#Adding layers to the model.
model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(4, activation='softmax'))
#Compiling and fitting model.
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
#Fitting the model
model.fit(predictors, target, epochs=10)

model.predict(test_data)