# Generated by Django 3.1.4 on 2020-12-20 09:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0012_auto_20201220_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
