from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lws.models.webiner_lists_model import WebinerListsModel
from lws.models.category_model import CategoryModel

@login_required
def webiner_list(request):
    webiners = WebinerListsModel.objects.all().order_by('date')
    categories = CategoryModel.objects.all().order_by('name')
    return render(request, 'lws/webiner_list.html', {'webiners': webiners, 'categories': categories})

@login_required
def register_webiner(request):
    
    return 0