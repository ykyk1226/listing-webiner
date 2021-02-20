from django.db import models
from users.models.custom_user import CustomUser
from lws.models.webinerListsModel import WebinerListsModel


class MylistsModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    webiner = models.ForeignKey(WebinerListsModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mylists'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'user',
                    'webiner'],
                name='unique_registration'),
        ]
