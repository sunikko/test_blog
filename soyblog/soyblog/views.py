import requests
import json

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("hello world")


def room(request, room_id):
    url = "http://api.zigbang.com/v1/items?detail=true&item_id="+room_id
    response = requests.get(url);
    return HttpResponse(response.content,
    content_type = "application/json",
    )


def news(request):
    search = request.GET.get("search")

    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
    news_dict = json.loads(response.text)

    content = "<h1>News</h1>" + \
        "<p>This is news page.</p>" + \
        "".join([
            "<h2>{title}</h2><img src={img_src}><p>{content}</p>".format(
                title=news.get("title"),
                img_src = news.get('image'),
                content = news.get('content'),
            )
            for news
            in news_dict["news"]
        ])
    return HttpResponse(content,)