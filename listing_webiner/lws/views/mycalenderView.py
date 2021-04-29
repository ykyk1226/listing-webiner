from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from lws.models.mylistsModel import MylistsModel
from lws.models.webinerListsModel import WebinerListsModel


class MycalenderView(generic.CreateView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        """mycalender表示処理、lws/mycalender.htmlを表示する。

        Returns:
            HttpResponse: lws/mycalender.htmlを表示するためのhttpレスポンス
        """
        mylists = MylistsModel.objects.select_related('webiner').filter(
            user=request.user).order_by('webiner_id__start_date')
        mywebiners = [mylist.webiner for mylist in mylists]
        return render(request, 'lws/mycalender.html',
                      {'mywebiners': mywebiners})
