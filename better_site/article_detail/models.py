from django.contrib.auth.models import User
from django.db import models
from main.models import Articles

class Comment(models.Model):

    user = models.CharField(max_length=100, default='some_user')
    content = models.TextField()
    post = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    likes_amount = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user} – {self.content}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'