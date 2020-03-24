import tweepy
import html
import os
from textblob import TextBlob
from classifier import *
from yandex_translate import YandexTranslate
import json

#Autenticación
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

#Objeto a través del cual vamos a realizar las llamadas a la API de Twitter
#Los parámetros wait_on_rate_limit se utilizan para que si se cumple con el cupo de tweets cargados, la app no se pare
#si no que espere un tiempo y cuando pueda continúe
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
clf = SentimentClassifier()
translator = YandexTranslate(os.getenv('YANDEX_KEY'))
#Obtener información sobre mi usuario
# data = api.me()
# print(json.dumps(data._json, indent=2))

#Obtener información sobre otro usuario
# data = api.get_user("nike")
# print(json.dumps(data._json, indent=2))

#Obtener el timeline
# for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(1):
#     print(json.dumps(tweet._json, indent=2))

#Buscar tweets


#     print(tweet._json["full_text"], tweet.text.encode("utf-8"))

def searchHashtag(hashtag, since_date=None, until_date=None):
    analysis_score = []
    for tweet in tweepy.Cursor(api.search, q=hashtag, tweet_mode="extended", since=since_date, until=until_date).items(4):
        analysis_score.append(sentiment_analysis(tweet))

    return analysis_score

def searchUser(user, since_date=None, until_date=None):
    analysis_score = []
    for tweet in tweepy.Cursor(api.search, q=user, tweet_mode="extended", since=since_date, until=until_date).items():
        analysis_score.append(sentiment_analysis(tweet))

    return analysis_score

def searchWord(word, since_date=None, until_date=None):
    analysis_score = []
    for tweet in tweepy.Cursor(api.search, q=word, tweet_mode="extended", since=since_date, until=until_date).items():
        analysis_score.append(sentiment_analysis(tweet))

    return analysis_score

def deEmojify(inputString):

    return inputString.encode('ascii', 'ignore').decode('ascii')

def sentiment_analysis(tweet):

    tweet=html.unescape(tweet._json["full_text"])
    tw_sinemoji = deEmojify(tweet)
    if not tw_sinemoji == '""' :
        if translator.detect(tw_sinemoji) == 'en':
            score = TextBlob(tweet).sentiment

        elif translator.detect(tw_sinemoji) == 'es':
            # Primera opción, utilizar libreria en español
            # score=clf.predict(tw_sinemoji)

            #Segunda opción traducir y utilizar librería en inglés
            translate = translator.translate(tw_sinemoji, 'en')
            score = TextBlob(translate["text"][0]).sentiment

    return score
