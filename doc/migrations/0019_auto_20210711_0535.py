# Generated by Django 2.2.6 on 2021-07-11 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0018_auto_20210711_0518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat_model',
            old_name='re_id',
            new_name='Sender_back',
        ),
        migrations.RenameField(
            model_name='chat_model',
            old_name='se_id',
            new_name='reciever_back',
        ),
    ]