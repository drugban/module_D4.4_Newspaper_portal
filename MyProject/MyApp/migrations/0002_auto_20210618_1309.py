# Generated by Django 3.2.4 on 2021-06-18 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]