# Computer_Vision_RPS

## Creation of keras model and labels for Computer vision

Teachable allows for fast and easy creation of image datasets which can then be trained, to create a keras model, i used the image model of the teachable machine.

Following the creation of the model, i initiliased four training classes, which were rock, paper, scissors and nothing.

Each image class was provided with around 500 images, i.e 500 images of various paper from different angles and intensities. The model training was set to 50 epochs which means each image was shown to the training model 50 times and further split into batchsized of 16. Where one  batch has approximently 32 images and once all 16 batches are done. One epoch is finished

The dataset provided various angles, depths and showability of the classes to provide various examples

## the environment and libraries being used

Now that we have the model, we have to decide which technology to use, in this project i have used opencv to capture the frame through your own webcame

This frame will then be passed on to our keras model, where the previously trained model is loaded in to the modelloader

## Creation of gameplay mechanics

The use of the time module, to capture the amount of seconds then it uses a 10 second counter to capture the frame from the webcame to pass on to the predicating model

we simulated the best of 3 rounds where the user or computer play 3 rounds and the winner is presented at the end


*to run the script you can just use python game_play.py in the terminal to run the project*
