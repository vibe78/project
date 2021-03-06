# Generated by Django 2.2.6 on 2021-07-12 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200729_1222'),
        ('doc', '0021_auto_20210711_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('Dr_notify', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dr_notify', to='user.patients')),
                ('pq_message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pq_message', to='user.Doctors')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
