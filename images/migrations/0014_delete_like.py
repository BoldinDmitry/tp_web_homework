# Generated by Django 2.2.6 on 2019-11-05 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0013_remove_image_is_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
