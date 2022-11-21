#%%
import cv2
from keras.models import load_model
import numpy as np
import time as t

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Output_window:
    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None


    def close_window(self):
        """
        Closes the window
    
    
        """
        self.cap.release() #realeses the cap object
        cv2.destroyAllWindows() #destroys all windows

    def update_window(self):
        cv2.imshow('frame', self.frame)    
        return self.frame

    def capture_window(self):
        """captures the window and normalise the image"""
        "reading the frame image show to the camera"
        ret, self.frame = self.cap.read()

        "normalise the image to send to prediction"    
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    # Normalize the image
        return normalized_image


class prediction_module:
    
    _convert = [ 
        "rock",
        "paper",
        "scissors",
        "nothing"
    ]

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.index_of_max_prediction = None
        pass
    def get_prediction(self, data):
         prediction = self.model.predict(data)
         self.index_of_max_prediction = np.argmax(prediction)
         converted_max_prediction = prediction_module._convert[self.index_of_max_prediction]

         return converted_max_prediction
    
def get_prediction():
    prediction_new = prediction_module()
    window = Output_window()
    timenow = t.time()
    print(timenow)
    localtimenow = t.localtime(timenow)
    localtimenow_inSeconds = localtimenow.tm_sec
    while True:
        
        normalized_image = window.capture_window()
        data[0] = normalized_image
        converted_prediction = prediction_new.get_prediction(data)
        window.update_window()
        print(converted_prediction)
        
        timedifference = t.time()
        
        timeddiff = t.localtime(timedifference)
        
        localtimediff_inSeconds = timeddiff.tm_sec
        
        if localtimenow_inSeconds - localtimediff_inSeconds >= 10:
            break
        
        elif localtimenow_inSeconds - localtimediff_inSeconds <= -10:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    window.close_window()
    print(f'you have chosen: {converted_prediction}')
    return converted_prediction
    



        



# %%
