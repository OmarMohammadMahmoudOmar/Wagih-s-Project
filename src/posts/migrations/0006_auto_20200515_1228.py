# Generated by Django 3.0.5 on 2020-05-15 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200513_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tumbnail',
            new_name='thumbnail',
        ),
    ]
