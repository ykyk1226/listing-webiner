from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from lws.models.webiner_lists import WebinerLists
from lws.models.category import Category

@login_required
def webiner_list(request):
    webiners = WebinerLists.objects.all().order_by('date')
    categories = Category.objects.all().order_by('name')
    return render(request, 'lws/webiner_list.html', {'webiners': webiners, 'categories': categories})