# Generated by Django 3.2.7 on 2021-09-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20210928_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]
