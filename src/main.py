import numpy as np
from skimage import io

from models import CompositeVGG19
from io_opt import read_images, check_target_exists


def main():
  samples = read_images()[5:]
  check_target_exists()

  for index, image in enumerate(samples):
    transformed = np.expand_dims(image, axis = 0) / 255.

    output = CompositeVGG19.get_output(
      transformed,
      "imagenet",
      filters = np.random.choice([64, 32, 16, 8])
    ).numpy()

    frame_name = f"../target/{str(index + 6).zfill(3)}.png"
    io.imsave(frame_name, np.squeeze(output, axis = 0))


if __name__ == "__main__":
  main()