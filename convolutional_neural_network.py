model = Sequential()

input_shape = (128, 128, 3)

model.add(Conv2D(16, kernel_size=(2, 2), strides=(1, 1),
                  activation='relu',
                  input_shape=input_shape))

model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(32, strides=(2, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))