import os
import random as py_random
import numpy as np
import tensorflow as tf
#from tensorflow.keras.utils import set_random_seed

RANDOM_SEED = 5353

def set_seed():
    os.environ['PYTHONHASHSEED'] = str(RANDOM_SEED)
    py_random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)
    #set_random_seed(RANDOM_SEED) # Equivalent to setting Python random, numpy and tensorflow seeds