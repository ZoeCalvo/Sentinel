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


#     print(tweet._json["full_text"], tweet.text.encode("utf-8"))

def searchHashtag(hashtag, since_date=None, until_date=None):
    for tweet in tweepy.Cursor(api.search, q=hashtag, tweet_mode="extended", since=since_date, until=until_date).items():
        print(tweet._json["full_text"])

    return None

def searchUser(user, since_date=None, until_date=None):
    for tweet in tweepy.Cursor(api.search, q=user, tweet_mode="extended", since=since_date, until=until_date).items():
        print(tweet._json["full_text"])

    return None

def searchWord(word, since_date=None, until_date=None):
    for tweet in tweepy.Cursor(api.search, q=word, tweet_mode="extended", since=since_date, until=until_date).items():
        print(tweet._json["full_text"])

    return None



if __name__ == "__main__":
    print("Selecciona una opción")
    print("1. Buscar tweets en un hashtag")
    print("2. Buscar tweets donde aparezca un usuario mencionado")
    print("3. Buscar tweets relacionados con una palabra")

    option = input("Introduce el número de la opción deseada: ")

    if option == "1":
        hashtag = input("Introduzca el hashtag con #: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        searchHashtag(hashtag, since_date, until_date)
    if option == "2":
        user = input("Introduzca el nombre del usuario con @: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        searchUser(user, since_date, until_date)
    if option == "3":
        word = input("Introduce la palabra: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        searchWord(word, since_date, until_date)
