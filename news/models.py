from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class News(models.Model):
    title = models.CharField(max_length=200)
    describtion = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos', null=True, blank=True)
    read_count = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, related_name = 'news')
    comments_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category} / {self.title}'

    class Meta:
        verbose_name_plural = "News"

class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "comments")
    news = models.ForeignKey(News, on_delete = models.CASCADE, related_name = "comments")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} / {self.news}'

