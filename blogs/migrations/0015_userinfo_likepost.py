# Generated by Django 3.2.7 on 2021-10-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20211002_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='likePost',
            field=models.ManyToManyField(to='blogs.Post'),
        ),
    ]