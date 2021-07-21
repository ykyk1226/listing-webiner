import json
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db import IntegrityError
from lws.models.webinerListsModel import WebinerListsModel
from lws.forms.registerWebinerForm import RegisterWebinerForm
from lws.models.mylistsModel import MylistsModel
import logging
from lws.utils.logMessageUtils import *
from lws.utils.clientMessageUtils import *


class RegisterWebinerView(generic.CreateView, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        """マイリストへwebinerを登録する。

        Args:
            request ([type]): request

        Returns:
            HttpResponse: 登録に成功:200、エラー:500
        """
        form = RegisterWebinerForm(request.POST)
        if form.is_valid():
            webiner = json.loads(form.cleaned_data['webiner_list'])
            try:
                MylistsModel.objects.create(
                        user=request.user,
                        webiner=WebinerListsModel(id=webiner['id'])
                    )
            except IntegrityError:
                logging.getLogger('lws').error(MSG_LOG_ERR_0002)
                return HttpResponse(status=500, content=MSG_CLIENT_0001)
            return HttpResponse(status=200)
        else:
            logging.getLogger('lws').error(MSG_LOG_ERR_0001)
            logging.getLogger('lws').error(form.errors)
            return HttpResponse(status=500, content=MSG_CLIENT_0002)
