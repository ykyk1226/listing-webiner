from django.db import models
from lws.models.categoryModel import CategoryModel
from lws.models.sourceSiteModel import SourceSiteModel

class WebinerListsModel(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    date = models.CharField(max_length=50)
    category_id = models.ForeignKey(CategoryModel, db_column='category_id', on_delete=models.DO_NOTHING)
    source_site_id = models.ForeignKey(SourceSiteModel, db_column='source_site_id', on_delete=models.DO_NOTHING)
    updated_at = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webiner_lists'