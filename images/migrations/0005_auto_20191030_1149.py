# Generated by Django 2.2.6 on 2019-10-30 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0004_auto_20191030_1136"),
    ]

    operations = [
        migrations.RenameField(
            model_name="creator", old_name="USERNAME_FIELD", new_name="username",
        ),
    ]
