from django.db import models

class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'