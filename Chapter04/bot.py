import rasa
import pathlib
import os

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent)
model = basedir + "/models"

endpoints = "endpoints.yml"
credentials = "credentials.yml"
#
rasa.run(model=model, endpoints=endpoints, credentials=credentials)
