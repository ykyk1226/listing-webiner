from django.contrib import admin
from lws.models.categoryModel import CategoryModel
from lws.models.sourceSiteModel import SourceSiteModel
from lws.models.webinerListsModel import WebinerListsModel
from lws.models.mylistsModel import MylistsModel

admin.site.register(CategoryModel)
admin.site.register(SourceSiteModel)
admin.site.register(WebinerListsModel)
admin.site.register(MylistsModel)
