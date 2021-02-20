from django.urls import path
from lws.views import listingWebinerView
from lws.views import RegisterWebinerView
from lws.views import MypageView

app_name = 'lws'
urlpatterns = [
    path(
        'webiner/',
        listingWebinerView.listingWebiner,
        name='webiner_list'),
    path(
        'mypage/',
        MypageView.as_view(),
        name='mypage'),
    path(
        'webiner/register',
        RegisterWebinerView.as_view(),
        name='register_webiner'),
]
