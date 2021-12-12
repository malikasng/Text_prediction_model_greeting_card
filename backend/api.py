# ./python_code/api.py
import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
from feedback_poem import feedbackPoem
from feedback_haiku import feedbackHaikus
from feedback_prosa import feedbackProsa

#import pretrained models ready for usage as functions
from poem_load_predict import poet
from haiku_load_predict import haiku
from prosa_load_predict import prosa
from prosa_sentence_upload_predict import prosa_sentence

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
#add input arguments from frontend
parser.add_argument("input_name")
parser.add_argument("input_relationship")
parser.add_argument("input_textform")
parser.add_argument("input_feedback")
parser.add_argument("input_newLine")

class Predict(Resource):
  def post(self):
    args = parser.parse_args()
    #convert args to strings so we can use them as inputs
    name_str = str(args["input_name"])
    relationship_str = str(args["input_relationship"])
    textform_str = str(args["input_textform"])
    feedback_str = str(args["input_feedback"])
    newLine_str = str(args["input_newLine"])
    #make an input list for our models
    input_list = []
    input_list.append(name_str)
    input_list.append(relationship_str)
    #the users choice determines which model predicts an output
    if textform_str.lower() == 'poem':
      feedbackPoem(feedback_str,newLine_str)
      outputs = poet(input_list[0], input_list[1])
    elif textform_str.lower() == 'haiku':
      feedbackHaikus(feedback_str, newLine_str)
      outputs = haiku(input_list[0], input_list[1])
    elif textform_str.lower() == 'prosa':
      feedbackProsa(feedback_str, newLine_str)
      outputs = prosa(input_list[0], input_list[1])
    elif textform_str.lower() == 'prosa_sentence':
      outputs = prosa_sentence(input_list[0])
    else:
      outputs = ['Things does not seem to work. Please restart the program.', 'Things does not seem to work. Please restart the program.','Things does not seem to work. Please restart the program.']

    return (outputs)
#prediction will be accessed via localhost:5000/predict
api.add_resource(Predict, "/predict")
if __name__ == "__main__":
  app.run(debug=True)