# Generated by Django 3.2.7 on 2021-10-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='musics'),
        ),
    ]
