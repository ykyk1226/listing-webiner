from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lws.models.webiner_lists import WebinerLists

@login_required
def webiner_list(request):
    webiners = WebinerLists.objects.all().order_by('date')
    return render(request, 'lws/webiner_list.html', {'webiners': webiners})