# Generated by Django 3.1.4 on 2020-12-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0014_auto_20201220_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_channel_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
