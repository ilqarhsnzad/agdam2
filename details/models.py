from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
# Create your models here.


class Logo(models.Model):
    title = models.CharField(max_length = 100)
    logo_image = models.ImageField(upload_to = 'logo')

    def __str__(self) -> str:
        return self.title

class BackgroundColor(models.Model):
    title = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.title

class Light(models.Model):
    light_user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "light")
    light = models.BooleanField(default = True)

    def __str__(self) -> str:
        return f'{self.light_user} / {self.light}'


        

class Reklam(models.Model):
    title = models.CharField(max_length = 500)
    reklam_owner = models.CharField(max_length = 200)
    describtion = models.TextField()
    image = models.ImageField(upload_to='reklam_images')
    video = models.FileField(upload_to='reklam_videos', null=True, blank=True)
    read_count = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title} / {self.reklam_owner}'
