from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Articles(models.Model):

    credit = 'credit'
    debit = 'debit'
    savings = 'savings'
    CATEGORIES = [(credit, 'Кредитки'), (debit, 'Дебетухи'), (savings, 'Накопилка')]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORIES, blank=False)
    content = models.TextField()
    photo = models.ImageField(upload_to="images")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    comments_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

