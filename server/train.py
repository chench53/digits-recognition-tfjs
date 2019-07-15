"""
    check https://www.tensorflow.org/tutorials
"""
import numpy as np
import tensorflow as tf

# https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
# I suggest you download this data file before run the model if you get a bad network.
data_path = r'./datasets/mnist.npz'
modle_path = r'./models/mnist'

def load_data(path):
    with np.load(path) as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']
        return (x_train, y_train), (x_test, y_test)

def train_modle(data):
    (x_train, y_train), (x_test, y_test) = data
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(512, activation=tf.nn.relu),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
    model.save('{}/model.h5'.format(modle_path))

data = load_data(data_path)
train_modle(data)