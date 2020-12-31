from django.urls import path
from lws.views import webiner

app_name = 'lws'
urlpatterns = [
    path('webiner/', webiner.webiner_list, name='webiner_list'),
]