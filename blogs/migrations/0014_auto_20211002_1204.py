# Generated by Django 3.2.7 on 2021-10-02 12:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0013_auto_20210929_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleImage', models.ImageField(blank=True, default='default/post.jpg', null=True, upload_to='post_images/')),
                ('title', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('good', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Program', 'Program'), ('Note', 'Note'), ('Travel', 'Travel')], default='Note', max_length=10)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='program',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='owner',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile',
            field=models.ImageField(blank=True, default='images/profile.jpg', null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
    ]
