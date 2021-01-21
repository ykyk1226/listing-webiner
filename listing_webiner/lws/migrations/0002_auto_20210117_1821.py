# Generated by Django 3.0.10 on 2021-01-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lws', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SourceSiteModel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'source_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WebinerListsModel',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=50)),
                ('updated_at', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'webiner_lists',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SourceSite',
        ),
        migrations.DeleteModel(
            name='WebinerLists',
        ),
    ]
