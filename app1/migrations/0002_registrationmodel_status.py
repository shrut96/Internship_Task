# Generated by Django 3.0.7 on 2021-01-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]