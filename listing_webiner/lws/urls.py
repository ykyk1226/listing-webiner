from django.urls import path
from lws.views import listingWebinerView
from lws.views import RegisterWebinerView

app_name = 'lws'
urlpatterns = [
    path('webiner/', listingWebinerView.listingWebiner, name='webiner_list'),
    path('webiner/register', RegisterWebinerView.as_view(), name='register_webiner'),
]