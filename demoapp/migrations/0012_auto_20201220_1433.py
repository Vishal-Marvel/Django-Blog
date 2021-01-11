# Generated by Django 3.1.4 on 2020-12-20 09:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demoapp', '0011_auto_20201219_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]