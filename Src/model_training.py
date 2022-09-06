# ***********************************************************************************************************
# Summary: Creation of the Model and Data preprocessing
#
# Requirements: Python Verison 3.7
#
# Author : Anto
# ***********************************************************************************************************
import tensorflow as tf
import numpy as np
import os
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from string import punctuation

# ***********************************************************************************************************
#
# Global Variables
#
# ***********************************************************************************************************

sequence_length = 100
BATCH_SIZE = 128
EPOCHS = 30

# ***********************************************************************************************************
#
#  fill in later
#
# ***********************************************************************************************************


def get_path(path):
    try:
        path = 'Src/scripts.txt'
        basename = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        text = text.lower()
        return text
    except Exception as e:
        raise Exception(str(e))

# ***********************************************************************************************************
#
#  fill in later
#
# ***********************************************************************************************************


def data_stats(text):
    try:
        n_char = len(text)
        unique_char = ''.join(sorted(set(text)))
        no_of_characters = ("No of Characater:", n_char)
        no_of_uniq_characters = ("No Of Unique Characters:", unique_char)
        return no_of_characters, no_of_uniq_characters

    except Exception as e:
        raise Exception(str(e))


def conv_2_int():
    # jfssdnfdjfs
    return
