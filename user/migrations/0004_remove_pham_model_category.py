# Generated by Django 2.2.6 on 2020-07-18 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_pham_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pham_model',
            name='category',
        ),
    ]
