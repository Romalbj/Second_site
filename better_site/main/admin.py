from django.contrib import admin
from .models import Articles
from article_detail.models import Comment

admin.site.register(Articles)
admin.site.register(Comment)

