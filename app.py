
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import json
import os
import numpy as np
import pandas as pd
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist 
import joblib

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

# Let's load the trained model
model = tf.keras.models.load_model("Nourris_Timothee_model_train.h5")
# let's create a label for each
class_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

# tries with loading datas from a csv file 
'''train_images_test = pd.read_csv("train_images.csv")
train_images_copy = train_images_test.drop(["label"], axis=1).copy()
train_images_copy = train_images_copy.to_numpy()
train_images_copy = train_images_copy.reshape(train_images_copy.shape[0], 28, 28)
datas = {"pixels": {train_images_copy[0].to_list()}}'''

# tries with loading datas from the mnist dataset
'''(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
first_image = train_images[0]
pixels = first_image.reshape(-1).tolist()
data = {"pixels": pixels}
response = requests.post("http://localhost:5000/classify", json=data)
print(response.json())'''



##########################################################################
## Routes
##########################################################################

@app.route("/api/hello")
def hello():
    """
    Return a hello message
    """
    return jsonify({"hello": "world"})
    

@app.route("/classify/<array>", methods=['GET', 'POST'])
def classify(array):
    
    image = json.loads(array, strict=False)

    # reshape and normalization of the inputed image
    image = np.array(image, dtype=np.float32)
    image = image.reshape(1, 28, 28)
    image = image.astype("float32")
    image /= 255

    # make the prediction
    prediction = model.predict(image)
    #print(prediction)
    label = int(np.argmax(prediction))
    #print(label)
    return jsonify({"prediction": label, 'label': class_labels[label]})

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run(port=5050, debug=True)
