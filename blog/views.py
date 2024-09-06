from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.all()

    context ={
        "posts": posts,
    }

    return render(request, "blog.html", context)
 
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def post(request):
    return render(request, "post.html")