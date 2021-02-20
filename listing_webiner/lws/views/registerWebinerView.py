import json
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db import IntegrityError
from lws.models.webinerListsModel import WebinerListsModel
from lws.forms.registerWebinerForm import RegisterWebinerForm
from lws.models.mylistsModel import MylistsModel


class RegisterWebinerView(generic.CreateView, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        """マイリストへwebinerを登録する。

        Args:
            request ([type]): request

        Returns:
            HttpResponse: 登録に成功したら200、失敗したら500
        """
        form = RegisterWebinerForm(request.POST)
        if form.is_valid():
            webiner_lists = json.loads(form.cleaned_data['webiner_lists'])
            mylists = []
            for webiner in webiner_lists:
                mylists.append(MylistsModel(
                    user=request.user,
                    webiner=WebinerListsModel(id=webiner['id']),
                ))
            try:
                MylistsModel.objects.bulk_create(mylists)
            except IntegrityError:
                return HttpResponse(status=500)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)
