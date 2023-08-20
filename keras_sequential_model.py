#Importing libraries
import keras
from keras.models import Sequential 
from keras.layers import Dense
#Creating a sequential model.
model = Sequential()
#Specifying the number of columns.
n_cols = concrete_data.shape[1]
#Adding layers to the model.
model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))
#Compiling and fitting model.
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(predictors,target)
#Creating predictions.
predictions = model.predict(test_data)