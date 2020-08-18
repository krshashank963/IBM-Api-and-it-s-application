# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:24:31 2020

@author: SHASHANK RAJPUT
"""


from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/7c16e553-b641-4325-8423-9c5df480684d"
iam_apikey_s2t = 'TqvCgbpGMC7yu9SYo4LZaD494DcGPW_3vphxgdI8UP-T'

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)


filename='Recording (online-audio-converter.com).mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    
response.result
from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")    

responserecognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)