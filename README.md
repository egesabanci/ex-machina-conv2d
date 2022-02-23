# Overview
<div style = "display: flex;">
  <img src = "https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src = "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  <img src = "https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
</div>

Applying 2D convolutions with extracted frames of the sample scene 
from Ex Machina movie for creating something artistic. Input images
are 14 extracted frames from the sample scene of the `Ex-machina` movie.
After the frame extraction, random 2D Convolutions has been applied. Then, these 14 images gathered back together for creating
the final GIF.

# Output
![Final GIF Output](https://raw.githubusercontent.com/egesabanci/ex-machina-conv2d/master/target/dist/output.gif)

# Network Architecture
```
          CompositeVGG19 - type: Sequential (Pretrained VGG19 based model)
                [first 3 layers with input shape of (720, 1280, 3)]
                                   (imagenet)
                                   ----------
                                        |
                                        |
                        Conv2D (with kernel size of (1, 1))
                                        |
                                        |
                                   ----------
                  Conv2D (with kernel size of (1, 1) and 3 filters)
                                        |
                                        |
                                   ----------
                        Conv2D (with kernel size of (1, 1))
                                        |
                                        |
                                   ----------
                      BatchNormalization (with default values)
```

# Lives on the Blockchain! :chains:
This project's output also minted and listed on OpenSea


[Get the item!](https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/95202647556271955572982637523054989277279704670720503865731697009783186915329/)