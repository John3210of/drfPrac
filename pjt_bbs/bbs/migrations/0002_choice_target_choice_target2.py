# Generated by Django 4.0.6 on 2022-08-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='target',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='choice',
            name='target2',
            field=models.IntegerField(default=1),
        ),
    ]