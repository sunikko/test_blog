from django.conf.urls import url
from django.contrib import admin

from django.http.response import HttpResponse

def home(request):
    return HttpResponse()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home)
]
