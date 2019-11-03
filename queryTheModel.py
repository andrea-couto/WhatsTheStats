'''
from google's documentation (just fixed some mistakes)
for this to work you need to set GOOGLE_AUTHORIZATION_... as a env variable
get the project and model id from google console
'''

import sys

import google.cloud
import google.cloud.automl_v1beta1 as ml

# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = ml.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  with open(file_path, 'rb') as ff:
    content = ff.read()
  print (get_prediction(content, project_id, model_id))

# Want to try it out ?? 
# remember to set a google_auth env var
# cd into this folder and run the following 

# python queryTheModel.py instagramIkea\2019-11-02_23-22-54_UTC.jpg 269382516877 ICN2966557138530336768