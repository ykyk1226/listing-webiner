from django.contrib import admin
from lws.models.category import Category
from lws.models.source_site import SourceSite
from lws.models.webiner_lists import WebinerLists
from lws.models.custom_user import CustomUser

admin.site.register(Category)
admin.site.register(SourceSite)
admin.site.register(WebinerLists)
admin.site.register(CustomUser)
