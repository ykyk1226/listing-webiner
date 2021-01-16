from django.contrib import admin
from lws.models.category_model import CategoryModel
from lws.models.source_site_model import SourceSiteModel
from lws.models.webiner_lists_model import WebinerListsModel

admin.site.register(CategoryModel)
admin.site.register(SourceSiteModel)
admin.site.register(WebinerListsModel)
