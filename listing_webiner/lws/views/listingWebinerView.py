from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lws.models.webinerListsModel import WebinerListsModel
from lws.models.categoryModel import CategoryModel

@login_required
def listingWebiner(request):
    webiners = WebinerListsModel.objects.all().order_by('date')
    categories = CategoryModel.objects.all().order_by('name')
    return render(request, 'lws/webiner_list.html', {'webiners': webiners, 'categories': categories})