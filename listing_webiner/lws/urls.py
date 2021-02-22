from django.urls import path
from lws.views import listingWebinerView
from lws.views import RegisterWebinerView
from lws.views import MycalenderView

app_name = 'lws'
urlpatterns = [
    path(
        'webiner/',
        listingWebinerView.listingWebiner,
        name='webiner_list'),
    path(
        'mycalender/',
        MycalenderView.as_view(),
        name='mycalender'),
    path(
        'webiner/register',
        RegisterWebinerView.as_view(),
        name='register_webiner'),
]
