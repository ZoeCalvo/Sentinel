import tweepy
import html
import os
from textblob import TextBlob
from classifier import *
from yandex_translate import YandexTranslate, YandexTranslateException
import json
from src.statistics_formulas import *
from src.database import *

#Autenticación
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
clf = SentimentClassifier()
translator = YandexTranslate(os.getenv('YANDEX_KEY'))
num_items = 50

def searchHashtag(hashtag, since_date=None, until_date=None):
    analysis_score = []

    for tweet in tweepy.Cursor(api.search, q=hashtag, tweet_mode="extended", since=since_date, until=until_date).items(num_items):
        tweet_ = html.unescape(tweet._json["full_text"])
        tw_sinemoji = deEmojify(tweet_)
        score = sentiment_analysis(tw_sinemoji)
        analysis_score.append(score)
        insert_dataHashtags(hashtag, tweet, tw_sinemoji, score)


    return analysis_score

def searchUser(user, since_date=None, until_date=None):
    analysis_score = []
    for tweet in tweepy.Cursor(api.search, q=user, tweet_mode="extended", since=since_date, until=until_date).items(num_items):
        tweet_ = html.unescape(tweet._json["full_text"])
        tw_sinemoji = deEmojify(tweet_)
        score = sentiment_analysis(tw_sinemoji)
        analysis_score.append(score)
        insert_dataUsersTw(user, tweet, tw_sinemoji, score)

    return analysis_score

def searchWord(word, since_date=None, until_date=None):
    analysis_score = []
    for tweet in tweepy.Cursor(api.search, q=word, tweet_mode="extended", since=since_date, until=until_date).items(num_items):
        tweet_ = html.unescape(tweet._json["full_text"])
        tw_sinemoji = deEmojify(tweet_)
        score = sentiment_analysis(tw_sinemoji)
        analysis_score.append(score)
        insert_dataWord(word, tweet, tw_sinemoji, score)

    return analysis_score

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def sentiment_analysis(tw_sinemoji):
    if not tw_sinemoji == '""' :
        try:
            if translator.detect(tw_sinemoji) == 'en':
                score = TextBlob(tw_sinemoji).sentiment.polarity
            else:
                score=clf.predict(tw_sinemoji)
        except YandexTranslateException:
            score = clf.predict(tw_sinemoji)

    return score
