import tweepy
import urllib.request
import re
import os
from os import environ

CON_KEY = environ['CON_KEY']
CON_SEC = environ['CON_SEC']
ACC_KEY = environ['ACC_KEY']
ACC_SEC = environ['ACC_SEC']

s= "El número de casos de COVID-19 en el mundo son"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CON_KEY, CON_SEC)
auth.set_access_token(ACC_KEY, ACC_SEC)

api = tweepy.API(auth)

fp = urllib.request.urlopen("http://coronavirus-19-api.herokuapp.com/countries/World")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

d = int(re.search(r'\d+', mystr).group())

v = s , d

api.update_status(v)