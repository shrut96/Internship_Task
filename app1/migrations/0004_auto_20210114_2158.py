# Generated by Django 3.0.7 on 2021-01-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210114_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]
