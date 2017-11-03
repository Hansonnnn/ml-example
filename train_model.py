"""@description LM Classifier"""
from keras.models import Sequential

from keras.layers.core import Dense, Activation  # neural network ,activation function

from read_data import get_data
from cm_plot import cm_plot

netfile = '/Users/hanzhao/PycharmProjects/ml-example/file/tmp/net.h5'  # path to model


def train_lm_classification():
    # init net
    net = Sequential()

    net.add(Dense(input_dim=3, output_dim=10))  # input to hide
    net.add(Activation('relu'))  # relu function between their
    net.add(Dense(input_dim=10, output_dim=1))  # hide to output
    net.add(Activation('sigmoid'))  # sigmoid's function between their
    net.compile(loss='binary_crossentropy', optimizer='adam')  ## use adam
    train = get_data()[0]

    net.fit(train[:, :3], train[:, 3], nb_epoch=1000, batch_size=1)  # train model ,1000's loop

    net.save(netfile)

    predict_result = net.predict_classes(train[:, :3]).reshape(len(train))  ## transform result

    cm_plot(train[:, 3], predict_result).show()


train_lm_classification()