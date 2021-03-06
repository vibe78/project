# Generated by Django 2.2.6 on 2021-07-10 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200729_1222'),
        ('doc', '0014_auto_20200731_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=90000, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.CharField(default=True, max_length=500)),
                ('reciever', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='user.Doctors')),
                ('sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='user.patients')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
