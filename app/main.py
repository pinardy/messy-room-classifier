from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
from tensorflow.keras.models import load_model


def getPrediction(filename):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    model = load_model('vgg_model.h5')

    preds = model.predict(x)
    result = preds[0][0]

    if result < preds[0][1]:
        label = "messy"
    else:
        label = "clean"
        
    return label