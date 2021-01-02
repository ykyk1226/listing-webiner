from django.contrib import admin
from users.models.custom_user import CustomUser

admin.site.register(CustomUser)