import numpy as np
from typing import Callable, Tuple

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.applications import VGG19


class CompositeVGG19(object):
  
  @staticmethod
  def get_output(
    input: np.ndarray,
    weights: str = "imagenet",
    filters: int = 3) -> tf.Tensor:
 
    """Returns output of composite pretrained
    VGG19 with given parameters

    Arguments:
      - input       : Input image for apply CNN - (np.ndarray)
      - weights     : training set - default: imagenet
      - filters     : Conv2D filter for feature extraction
    """

    vgg_layers = VGG19(
      include_top = False,
      input_shape = (720, 1280, 3),
      weights = weights
    ).layers[:3]

    custom_layers = [
      layers.Conv2D(filters = filters, kernel_size = (1, 1)),
      layers.Conv2D(filters = 3, kernel_size = (1, 1)),
      layers.BatchNormalization()
    ]

    model = models.Sequential(vgg_layers + custom_layers)

    return model(input)


class BasicCNN(object):

  @staticmethod
  def get_output(
    input: np.ndarray,
    filters: int,
    kernel_size: Tuple,
    activation: Callable) -> tf.Tensor:
    
    """Returns output of BasicCNN
    with given input parameters

    Arguments:
      - input       : Input image for apply CNN - (np.ndarray)
      - filters     : Convolution filters for 1 step - int
      - kernel_size : Kernel size (pool size) for receptive field
      - activation  : Activation function as a callable - Callable
    """
    assert len(kernel_size) == 2, "Kernel size must be 2 dimensional"

    x = layers.Conv2D(
      filters = filters,
      kernel_size = kernel_size,
      activation = activation,
    )(input)

    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    output = layers.BatchNormalization()(x)

    return output