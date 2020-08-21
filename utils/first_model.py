from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


TRAIN_DATA_URL = 'https://github.com/SMATEO49/predictable-api/blob/master/data/bitcoin.csv'

dataset = loadtxt('../data/bitcoin.csv', delimiter=',')

X = dataset[:, 0:7]
Y = dataset[:, 7]

model = Sequential()
model.add(Dense(7, activation="relu", input_dim=7))
model.add(Dense(7, activation="relu"))
model.add(Dense(7, activation="relu"))
model.add(Dense(7, activation="relu"))
model.add(Dense(1, activation="relu"))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=20, batch_size=30)

_, accuracy = model.evaluate(X, Y)
print('Accuracy: %.2f' % (accuracy*100))
