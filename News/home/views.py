from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
# Create your views here.
# Will Implement Later
# def countrySearch(request):
#         country = request.GET.get('countrySearch')
#         if country :
#             data = requests.get(f'https://newsapi.org/v2/country={country}&apiKey=e97129159fd74b81a61b043e571ff5d2').json()
#         status = data["status"]
#         if status == "error" :
#             return render(request,"webDown.html")
#         n = int(data["totalResults"])
#         results = data["articles"]
#         # TITLES OF NEWS
#         titles=[]
#         for j in results :
#             titles.append(j["title"])
#         # print(titles)
#         # SOURCES OF NEWS
#         sources = []
#         for j in results :
#             sources.append(j["source"]["name"])
#         # print(sources)

#         # AUTHORS OF NEWS
#         authors = []
#         for j in results :
#             # if j["author"] == "None":
#             #     j["author"] =""
#             authors.append(j["author"])
#         # print(authors)
        
#         # DESCRIPTIONS OF NEWS
#         descriptions = []
#         for j in results :
#             descriptions.append(j["description"])
#             descriptions.append(j["description"])
#         # print(descriptions)

#         # URLS OF NEWS
#         URLS = []
#         for j in results :
#             URLS.append(j["url"])
#         # print(URLS)

#         # URL_IMAGES OF NEWS
#         urlToImages = []
#         for j in results :
#             urlToImages.append(j["urlToImage"])
#         # print(urlToImages)

#         # TIME OF NEWS
#         TIMES = []
#         for j in results :
#             TIMES.append(j["publishedAt"])
#         # print(TIMES)

#         # contents OF NEWS
#         contentS = []
#         for j in results :
#             contentS.append(j["content"])
#         # print(contentS)

#         dict ={
#             "n":n,
#             "title" : titles,
#             # DONE
#             "author" : authors,
#             # Not Going To Include
#             "source" : sources,
#             # Not Going To Include
#             "content" :contentS,
#             "description" : descriptions,
#             "time" :TIMES,
#             "image" : urlToImages,
#             "url" :URLS,
#             "result":results,
#         }
#         return render(request,"home.html",dict)

def world(request):
    # data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e97129159fd74b81a61b043e571ff5d2').json()
    data = requests.get('https://newsapi.org/v2/everything?q=keyword&apiKey=e97129159fd74b81a61b043e571ff5d2').json()
    status = data["status"]
    if status == "error" :
        return render(request,"webDown.html")
    n = int(data["totalResults"])
    results = data["articles"]

    # TITLES OF NEWS
    titles=[]
    for j in results :
        titles.append(j["title"])
    # print(titles)

    # SOURCES OF NEWS
    sources = []
    for j in results :
        sources.append(j["source"]["name"])
    # print(sources)

    # AUTHORS OF NEWS
    authors = []
    for j in results :
        # if j["author"] == "None":
        #     j["author"] =""
        authors.append(j["author"])
    # print(authors)
    
    # DESCRIPTIONS OF NEWS
    descriptions = []
    for j in results :
        descriptions.append(j["description"])
        descriptions.append(j["description"])
    # print(descriptions)

    # URLS OF NEWS
    URLS = []
    for j in results :
        URLS.append(j["url"])
    # print(URLS)

    # URL_IMAGES OF NEWS
    urlToImages = []
    for j in results :
        urlToImages.append(j["urlToImage"])
    # print(urlToImages)

    # TIME OF NEWS
    TIMES = []
    for j in results :
        TIMES.append(j["publishedAt"])
    # print(TIMES)

    # contents OF NEWS
    contentS = []
    for j in results :
        contentS.append(j["content"])
    # print(contentS)

    dict ={
        "n":n,
        "title" : titles,
        # DONE
        "author" : authors,
        # Not Going To Include
        "source" : sources,
        # Not Going To Include
        "content" :contentS,
        "description" : descriptions,
        "time" :TIMES,
        "image" : urlToImages,
        "url" :URLS,
        "result":results,
    }
    return render(request,"home.html",dict)
def IndiaNews(request):
    data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e97129159fd74b81a61b043e571ff5d2').json()
    # data = requests.get('https://newsapi.org/v2/everything?q=keyword&apiKey=e97129159fd74b81a61b043e571ff5d2').json()
    status = data["status"]
    if status == "error" :
        return render(request,"webDown.html")
    n = int(data["totalResults"])
    results = data["articles"]

    # TITLES OF NEWS
    titles=[]
    for j in results :
        titles.append(j["title"])
    # print(titles)

    # SOURCES OF NEWS
    sources = []
    for j in results :
        sources.append(j["source"]["name"])
    # print(sources)

    # AUTHORS OF NEWS
    authors = []
    for j in results :
        # if j["author"] == "None":
        #     j["author"] =""
        authors.append(j["author"])
    # print(authors)
    
    # DESCRIPTIONS OF NEWS
    descriptions = []
    for j in results :
        descriptions.append(j["description"])
    # print(descriptions)

    # URLS OF NEWS
    URLS = []
    for j in results :
        URLS.append(j["url"])
    # print(URLS)

    # URL_IMAGES OF NEWS
    urlToImages = []
    for j in results :
        urlToImages.append(j["urlToImage"])
    # print(urlToImages)

    # TIME OF NEWS
    TIMES = []
    for j in results :
        TIMES.append(j["publishedAt"])
    # print(TIMES)

    # contents OF NEWS
    contentS = []
    for j in results :
        contentS.append(j["content"])
    # print(contentS)

    dict ={
        "n":n,
        "title" : titles,
        # DONE
        "author" : authors,
        # Not Going To Include
        "source" : sources,
        # Not Going To Include
        "content" :contentS,
        "description" : descriptions,
        "time" :TIMES,
        "image" : urlToImages,
        "url" :URLS,
        "result":results,
    }
    return render(request,"home.html",dict)

def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")


