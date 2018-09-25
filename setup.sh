#!/bin/bash

# to run the model, all of the following packages must be installed
# all the user needs to do is call ./setup.sh to run the model

sudo easy_install pip3
pip3 install scipy
pip3 install argparse
pip3 install numpy
pip3 install keras
pip3 install tensorflow
pip3 install Pillow
pip3 install opencv-python

python3 draw.py
