from django.core import validators
from django.db import models
# Create your models here.
from django.dispatch import receiver
import os
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

def resize_image(imageField, width=None):
    img = Image.open(imageField)
    w, h = img.size
    if not width:
        rw = 710.0 / w
    else:
        rw = width / w
    h = h * rw
    if h > 800:
        h = 800
    img = img.resize((710, int(h)))
    return img
    

class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titleImage = models.ImageField(blank=True, null=True, upload_to="post_images/", default="default/post.jpg")
    title = models.TextField(blank=True, null=True)
    date = models.DateField()   
    content = RichTextField(blank=True, null=True)
    good = models.IntegerField(default=0)
    category = models.CharField(
        max_length=10,
        choices=[("Food", "Food"), ("Program", "Program"), ("Note", "Note"), ("Travel", "Travel")],
        default="Note"
    )

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img = resize_image(self.titleImage)
        img.save(self.titleImage.path)

    def __str__(self) -> str:
        return self.title

    

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=[("F", "Female"), ("M", "Male"), ("X", "Secret")]
    )
    # description = models.CharField(max_length=1024)
    description = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    linkin = models.CharField(max_length=128, blank=True, null=True)
    facebook = models.CharField(max_length=128, blank=True, null=True)
    instagram = models.CharField(max_length=128, blank=True, null=True)
    github = models.CharField(max_length=128, blank=True, null=True)
    degree = models.CharField(
        max_length=2,
        choices=[("N", "None"), ("B", "Bachelor"), ("M", "Master"), ("D", "Doctor")],
        default="N"
    )
    profile = models.ImageField(null=True, blank=True, upload_to="images/", default='images/profile.jpg')
    likePost = models.ManyToManyField(Post, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    

class Music(models.Model):

    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='musics')
    cover = models.ImageField(null=True, blank=True, upload_to="musics", default="musics/default.png")
    link = models.CharField(null=True, max_length=200)

    paginator_num = 2

    def save(self, *args, **kwargs):
        super(Music, self).save(*args, **kwargs)
        img = resize_image(self.cover, 800)
        img.save(self.cover.path)

    def __str__(self) -> str:
        return self.title + '_' + self.author 























@receiver(models.signals.post_delete, sender=UserInfo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)

@receiver(models.signals.pre_save, sender=UserInfo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = UserInfo.objects.get(pk=instance.pk).profile
    except UserInfo.DoesNotExist:
        return False

    new_file = instance.profile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=Music)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.cover:
        if os.path.isfile(instance.cover.path):
            os.remove(instance.cover.path)

@receiver(models.signals.pre_save, sender=Music)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Music.objects.get(pk=instance.pk).cover
    except Music.DoesNotExist:
        return False

    new_file = instance.cover
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=Music)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Music)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Music.objects.get(pk=instance.pk).file
    except Music.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

