# Generated by Django 3.1.4 on 2021-01-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=400)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
