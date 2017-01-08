import requests
from django.http.response import HttpResponse

def home(request):
    return HttpResponse("hello world")


def room(request, room_id):
    url = "http://api.zigbang.com/v1/items?detail=true&item_id="+room_id
    response = requests.get(url);
    return HttpResponse(response.content)

