from django.db import models

class SourceSite(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    site_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'source_site'