"""
PicMetric Flask API: Given a single images or batch
of images, analyzes the images and returns a JSON with
summary information about the image(s) and batch.
"""

from flask import Flask, jsonify, request, render_template
import json
import pickle


app = Flask(__name__)

MODEL = pickle.load('model.pkl') # ?? To do: Get model as pickled string

@app.route('/summary', methods=['POST']))
def summary():
    """
    Analyzes 1 image and returns summary information
    about the image.
    """
    # Get incoming request:
    request = request.json # or flask.request.json, or request.get_json ??

    people_present = MODEL.predict(image)
    image_summary = jsonify(
                            {
                            'user_id' : user_id,
                            'image_id' : image_id,
                            'batch_id' : batch_id,
                            'people_present' : prediction_people_present
                            }
                           )

    return image_summary

# Route at /resetdb that clears and resets our database:
@app.route('/batch_img_summary', methods=['POST'])
def batch_img_summary():
    """
    Analyzes a batch of multiple images, and returns
    summary information about the batch and the images.
    """
    # Get incoming request:
    request = request.json

    # ?? To do

    batch_summaries = {}
    for image in batch:
        image_summary = jsonify(
                                {
                                'user_id' : user_id,
                                'image_id' : image_id,
                                'batch_id' : batch_id,
                                'people_present' : prediction_people_present
                                }
                               )
        batch_summaries[image_id] = image_summary

    return batch_summaries

# While debugging:
if __name__ == "__main__":
    app.run(debug=True, port=8080)
