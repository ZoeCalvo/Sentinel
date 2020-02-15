import tweepy
from claves import *
import json

#Autenticación
access_token = access_token
access_token_secret = access_token_secret
api_key = api_key
api_secret_key = api_secret_key

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

#Objeto a través del cual vamos a realizar las llamadas a la API de Twitter
#Los parámetros wait_on_rate_limit se utilizan para que si se cumple con el cupo de tweets cargados, la app no se pare
#si no que espere un tiempo y cuando pueda continúe
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

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
# for tweet in tweepy.Cursor(api.search, q="viernes", tweet_mode="extended").items(1):
#     print(json.dumps(tweet._json, indent=2))
for tweet in tweepy.Cursor(api.search, q="#Estudio3Sector2019", tweet_mode="extended").items(1):
#     print(json.dumps(tweet._json, indent=2))
    print(tweet._json["full_text"])
