from django.contrib import admin

# Register your models here.

from main.models import Post
from comments.models import Comment
admin.site.register(Post)
admin.site.register(Comment)