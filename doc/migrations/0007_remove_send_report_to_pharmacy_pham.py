# Generated by Django 2.2.6 on 2020-07-24 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0006_book_apointment_model_uu_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send_report_to_pharmacy',
            name='Pham',
        ),
    ]