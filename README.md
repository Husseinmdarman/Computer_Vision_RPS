# Computer_Vision_RPS

## Milestone 1

### Creation of keras model and labels for Computer vision

To create a keras model, i used the image model of the teachable machine. Teachable allows for fast and easy creation of image datasets which can then be trained

Following the creation of the model, i initiliased four training classes, where the classes were rock, paper, scissors and nothing.

Where each image class was provided with around 500 images, and the model training was set to 50 epochs which means each image was shown to the training model 50 times over this is further split into batch sizes of 16. Where means one batch has approximantly 32 images and once all 16 batchs are done means that one epoch has finished

The dataset provided various angles, depths and showability of the classes to provide various examples