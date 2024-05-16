from django.db import models

class Articles(models.Model):

    credit = 'credit'
    debit = 'debit'
    savings = 'savings'
    CATEGORIES = [(credit, 'Кредитки'), (debit, 'Дебетухи'), (savings, 'Накопилка')]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORIES, blank=False, default=1)
    content = models.TextField()
    photo = models.ImageField(upload_to="images")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    likes_amount = models.IntegerField()
    comments_amount = models.IntegerField()

    def __str__(self):
        return self.title
