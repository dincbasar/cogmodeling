# Mute tensorflow debugging information on console
import os
import sys
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from scipy.misc import imsave, imread, imresize
import numpy as np
import argparse
from keras.models import model_from_yaml
import re
import base64
import pickle

#filename = sys.argv[1]

def load_model():
    # load YAML and create model
    yaml_file = open('training/bin/model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    model = model_from_yaml(loaded_model_yaml)

    # load weights into new model
    model.load_weights('training/bin/model.h5')
    return model

model = load_model()

def predict(filename):
    global model
    # Local functions
    def crop(x):
        # Experimental
        _len = len(x) - 1
        for index, row in enumerate(x[::-1]):
            z_flag = False
            for item in row:
                if item != 0:
                    z_flag = True
                    break
            if z_flag == False:
                x = np.delete(x, _len - index, 0)
        return x

    # read parsed image back in 8-bit, black and white mode (L)
    x = imread(filename, mode='L')
    x = np.invert(x)

    ### Experimental
    # Crop on rows
    x = crop(x)
    x = x.T
    # Crop on columns
    x = crop(x)
    x = x.T

    # Visualize new array
    imsave('resized.png', x)
    x = imresize(x,(28,28))

    # reshape image data for use in neural network
    x = x.reshape(1,28,28,1)

    # Convert type to float32
    x = x.astype('float32')

    # Normalize to prevent issues with model
    x /= 255

    # Predict from model
    out = model.predict(x)

    mapping = pickle.load( open( "training/bin/mapping.p", "rb" ) )

    # Generate response
    x = (int(np.argmax(out, axis=1)[0]))
    print(x)
    print(mapping[x])
    response = {'prediction': chr(mapping[x]),
                'confidence': str(max(out[0]) * 100)[:6]}

    print(response)
    return response

