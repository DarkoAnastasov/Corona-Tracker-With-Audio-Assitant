import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time

API_KEY = 'tbGPHOXbSmZ9'
PROJECT_TOKEN = 'tcYNdBv5qarp'
RUN_TOKEN = 't9YOgJQj-yqe'


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

 

