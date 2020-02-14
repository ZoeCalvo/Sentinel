from InstagramAPI import InstagramAPI
import json
import re
from claves import *
import time
from datetime import date, datetime, timedelta

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

def investigar():
    investigar = []
    following = api.getTotalFollowings(user_id)
    investigar.append(following)
    f2 = parse(investigar[0])
    numero = 0

    for j in range(len(f2)):
        if numero >= 0:
            IDpersona = f2[j].get("pk")
            getMediaData(IDpersona)
        else:
            numero += 1
    return None

def getMediaData(IDpersona):
    try:
        all_posts = api.getTotalUserFeed(IDpersona)
        flag = True

        for post in all_posts:
            while flag:
                if "id" in post:
                    IDpublicacion = str(post["id"])

                if "caption" in post:
                    if post["caption"]:
                        if "text" in post["caption"]:
                            txt_sinEmojis = deEmojify(post["caption"]["text"])
                            texto = str(txt_sinEmojis.encode("utf8"))

                if "taken_at" in post:
                    timestamp = str(post["taken_at"])

                    fecha = datetime.fromtimestamp(float(timestamp))

                print ("idpubl: ", IDpublicacion)
                print("txt: ", texto)
                print("fecha: ", fecha)
                getMediaHashtag(IDpublicacion, texto)
                getComments(IDpublicacion)
                flag = False

    except:
        pass
    return None


def getMediaHashtag(media_id, texto):
    total_hashtags = re.findall(r"\#(\w+)", texto)

    for hashtag in total_hashtags:
        print(hashtag)

    return None


def getComments(media_id):
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
           comentario = str(sin_emoji.encode("utf8"))
           print(comentario)

    return None


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def explore():
    explora = []
    captions = []
    _ = api.explore()
    for publicacion in api.LastJson['items']:
        explora.append(publicacion)

    for publicacion in explora:
        if "media" in publicacion:
            if publicacion["media"]:
                if "id" in publicacion["media"]:
                    IDpublicacion = str(publicacion["media"]["id"])

                if "caption" in publicacion["media"]:
                    captions.append(publicacion["media"]["caption"])
                    for txt in captions:
                        if txt is not None:
                            if "text" in txt:
                                texto = str(txt["text"])
                                print(texto)
                        getMediaHashtag(IDpublicacion, texto)
    return None


if __name__ == "__main__":
    # nombre = input("Introduce tu nombre: ")
    # passw = input("Introduce tu contrasena: ")

    api = InstagramAPI(user_ig, pass_ig)
    api.login()
    user_id = api.username_id
    followings = input("¿Quieres mirar a quién sigues?: (Y/N) ")
    if followings == "Y":
        investigarFollowings = investigar()
    else:
        explorar = explore()


