# Generated by Django 3.1.5 on 2021-01-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0008_auto_20210105_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
