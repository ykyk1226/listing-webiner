from django.urls import path
from lws.views import webiner_view

app_name = 'lws'
urlpatterns = [
    path('webiner/', webiner_view.webiner_list, name='webiner_list'),
    path('webiner/register', webiner_view.register_webiner, name='register_webiner'),
]