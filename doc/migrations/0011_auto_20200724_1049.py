# Generated by Django 2.2.6 on 2020-07-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0010_auto_20200724_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm_drug',
            name='confirm',
            field=models.CharField(blank=True, default='Pending', max_length=120, null=True),
        ),
    ]
