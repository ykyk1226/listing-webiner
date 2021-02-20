from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from lws.models.mylistsModel import MylistsModel
from lws.models.webinerListsModel import WebinerListsModel


class MypageView(generic.CreateView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        mylists = MylistsModel.objects.select_related('webiner').filter(
            user=request.user).order_by('webiner_id__date')
        mywebiners = [mylist.webiner for mylist in mylists]
        return render(request, 'lws/mypage.html',
                      {'mywebiners': mywebiners})
