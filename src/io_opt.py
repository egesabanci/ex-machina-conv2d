import os
from typing import List

import numpy as np
from skimage import io


class Paths:  
  FRAMES = os.path.join("..", "frames")
  TARGET = os.path.join("..", "target")


def read_images() -> List[np.ndarray]:
  frame_names = sorted(os.listdir(Paths.FRAMES))
  
  images = map(
    lambda x: io.imread(os.path.join(Paths.FRAMES, x)),
    frame_names
  )

  return list(images)


def check_target_exists() -> None:
  if "target" not in os.listdir(os.path.join("..")):
    os.system("mkdir ../target")

  return None