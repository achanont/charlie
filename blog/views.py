from django.shortcuts import render
from django.utils import timezone
from .models import Post #import model post (from models.py) so that we can include code from different files
from django.shortcuts import render, get_object_or_404


def post_list(request):
    #created a QuerySet named 'posts'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #'blog/post_list.html' refers to a template file
    #parameter in {} needs a name so that we can allow templates to use
    return render(request, 'blog/post_list.html', {'posts': posts})

# post's detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
