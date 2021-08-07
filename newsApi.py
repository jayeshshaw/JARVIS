import requests

def getNews(q):
    if(q == None):
        mainUrl = "https://newsapi.org/v2/top-headlines?country=in&apiKey=89a4fe43466c4b6595adc53c77ee1f21"
    else :
        mainUrl = "https://newsapi.org/v2/everything?q="+q+"&apiKey=89a4fe43466c4b6595adc53c77ee1f21"    

    pages = requests.get(mainUrl).json()
    # print(pages)

    article = pages['articles']

    results = []

    for ar in article:
        results.append(ar['title'])
    return results
    # for i in range(len(results)):
    #     print(i+1, results[i])
# category = input("Enter the category of news")
# if(category == ' '):
#     category = None
# print(getNews(category))