# Generated by Django 3.2.7 on 2021-09-27 13:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0008_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='good',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='good',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='good',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='recommend',
            field=models.CharField(choices=[('B', 'Bad'), ('F', 'Fine'), ('G', 'Good'), ('E', 'Excellent'), ('A', 'Awesome')], default='G', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='titleImage',
            field=models.ImageField(blank=True, default='default/note.jpg', null=True, upload_to='food_images/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='degree',
            field=models.CharField(choices=[('B', 'Bachelor'), ('M', 'Master'), ('D', 'Doctor')], default='B', max_length=2),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleImage', models.ImageField(blank=True, default='default/note.jpg', null=True, upload_to='food_images/')),
                ('title', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('good', models.IntegerField(default=0)),
                ('recommend', models.CharField(choices=[('B', 'Bad'), ('F', 'Fine'), ('G', 'Good'), ('E', 'Excellent'), ('A', 'Awesome')], default='G', max_length=2)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleImage', models.ImageField(blank=True, default='default/note.jpg', null=True, upload_to='food_images/')),
                ('title', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('good', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
