from django.db import models
from lws.models.category import Category
from lws.models.source_site import SourceSite

class WebinerLists(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    date = models.CharField(max_length=50)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    source_site = models.ForeignKey(SourceSite, models.DO_NOTHING)
    updated_at = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webiner_lists'