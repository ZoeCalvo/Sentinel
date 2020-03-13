from InstagramAPI import InstagramAPI
import json
import re
import os
import html
from textblob import TextBlob
from googletrans import Translator
from classifier import *
import time
from datetime import date, datetime, timedelta


clf = SentimentClassifier()
translator = Translator()

def parse(lst):
    listReturn=[]
    for i in lst:
        d={}
        d["pk"]=i.get("pk")
        d["username"]=i.get("username")
        d["full_name"]=i.get("full_name")
        d["is_private"]=i.get("is_private")
        listReturn.append(d)

    return listReturn


def research(api,user_id):
    research = []
    following = api.getTotalFollowings(user_id)
    research.append(following)
    f2 = parse(research[0])
    num = 0

    for j in range(len(f2)):
        if num >= 0:
            user_id = f2[j].get("pk")
            user_name = f2[j].get("username")
            print("id: ", user_id)
            print("name: ", user_name)
            #getMediaData(user_id)
        else:
            num += 1
    return None


def getMediaData(api,userId):
    try:
        all_posts = api.getTotalUserFeed(userId)
        flag = True

        for post in all_posts:
            # while flag:
            if "id" in post:
                idPost = str(post["id"])

            if "caption" in post:
                if post["caption"]:
                    if "text" in post["caption"]:
                        txt_sinEmojis = deEmojify(post["caption"]["text"])
                        text = str(txt_sinEmojis.encode("utf8"))

            if "taken_at" in post:
                timestamp = str(post["taken_at"])

                datePost = datetime.fromtimestamp(float(timestamp))

            print ("idpost: ", idPost)
            print("txt: ", text)
            # print("date: ", datePost)
            # getMediaHashtag(idPost, text)
            getComments(idPost)


    except:
        pass
    return None


def getMediaHashtag(media_id, text):
    total_hashtags = re.findall(r"\#(\w+)", text)

    for hashtag in total_hashtags:
        print(hashtag)

    return None


def getComments(api, media_id):
    has_comments = True
    max_id = ''
    comments = []

    while has_comments:
        _ = api.getMediaComments(media_id, max_id=max_id)
        # comments' page come from older to newer, lets preserve desc order in full list
        for c in reversed(api.LastJson['comments']):
            comments.append(c)
        has_comments = api.LastJson.get('has_comments', False)

    for c in comments:
       if "text" in c:
           sin_emoji = deEmojify(c["text"])
           comment = json.dumps(sin_emoji)
           sentiment_analysis(comment)

    return None


def sentiment_analysis(comment):

    comment = html.unescape(comment)

    if translator.detect(comment).lang == 'en':
        txt = TextBlob(comment)
        print(comment + "\n", txt.sentiment)
    elif translator.detect(comment).lang == 'es':
        #Primera opción utilizar la librería en español
        # print(comment + '\n' + '%.5f' % clf.predict(comment))

        # Segunda opción, traducir y utilizar librería en inglés
        translate = translator.translate(comment, dest='en')
        trans = TextBlob(translate.text)
        print(comment + "\n", trans.sentiment)

    return None

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def explore(api):
    explore = []
    captions = []
    _ = api.explore()
    for post in api.LastJson['items']:
        explore.append(post)

    for post in explore:
        if "media" in post:
            if post["media"]:
                if "id" in post["media"]:
                    postId = str(post["media"]["id"])

                if "caption" in post["media"]:
                    captions.append(post["media"]["caption"])
                    for txt in captions:
                        if txt is not None:
                            if "text" in txt:
                                text = str(txt["text"])
                                print(text)
                        getMediaHashtag(postId, text)
    return None

def search_users(api, userName):
    _ = api.searchUsername(userName)
    userId = api.LastJson["user"]["pk"]
    #

    return userId


def main():
    user_ig = os.getenv('USER_IG')
    pass_ig = os.getenv('PASSWD_IG')
    api = InstagramAPI(user_ig, pass_ig)
    api.login()

    return api



    # followings = input("¿Quieres mirar a quién sigues?: (Y/N) ")
    # if followings == "Y":
    #     user = input("Introduce tu nombre de usuario sin @: ")
    #     userId = search_users(user)
    #     research(userId)
    # else:
    #     ans = input("Quieres buscar a un usuario concreto?: (Y/N) ")
    #     if ans == "Y":
    #         user = input("Introduce el nombre del usuario sin @: ")
    #         userId = search_users(user)
    #         getMediaData(userId)
    #     else:
    #         explore()


