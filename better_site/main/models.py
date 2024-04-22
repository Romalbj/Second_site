from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="images")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    likes_amount = models.IntegerField()
    comments_amount = models.IntegerField()
