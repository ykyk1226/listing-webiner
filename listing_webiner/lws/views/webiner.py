from django.shortcuts import render
from lws.models.webiner_lists import WebinerLists

def webiner_list(request):
    webiners = WebinerLists.objects.all().order_by('date')

    return render(request, 'lws/webiner_list.html', {'webiners': webiners})