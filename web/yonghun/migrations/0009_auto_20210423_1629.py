# Generated by Django 3.1.6 on 2021-04-23 07:29

from django.db import migrations
import yonghun.models


class Migration(migrations.Migration):

    dependencies = [
        ('yonghun', '0008_auto_20210423_1628'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', yonghun.models.UserManager()),
            ],
        ),
    ]
