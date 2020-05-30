# Generated by Django 3.0.6 on 2020-05-13 13:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_ar',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='overview_ar',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ar',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
