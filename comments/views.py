from django.shortcuts import render
from comments.models import Comment


# Create your views here.


def comments_list(request):
    posts = Comment.objects.all()
    return render(request, 'comments/comments.html', context={'comments': posts})
