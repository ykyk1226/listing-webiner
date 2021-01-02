from django.shortcuts import render, redirect
from lws.models.webiner_lists import WebinerLists

def webiner_list(request):
    if request.user.is_authenticated:
        webiners = WebinerLists.objects.all().order_by('date')
        return render(request, 'lws/webiner_list.html', {'webiners': webiners})
    else:
        return redirect(to='/users/login')