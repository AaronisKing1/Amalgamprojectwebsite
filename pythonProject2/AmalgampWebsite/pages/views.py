from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post, Comment

def pages_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "pages/index.html", context)
def pages(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def pages_category(request, category):
    posts = Post.objects.filter(
      categories__name__contains=category
    ).order_by("-created_on")
    context = {
      "category": category,
      "posts": posts,
    }
    return render(request, "pages/category.html", context)


def pages_detail(request, pk):
  post = Post.objects.get(pk=pk)
  comments = Comment.objects.filter(post=post)
  context = {
    "post": post,
    "comments": comments,
  }

  return render(request, "pages/detail.html", context)

def home(request):
    return render(request, "index.html")

def games(request):
    return render(request, "games.html")

def aboutme(request):
    return render(request, "aboutme.html")

def art(request):
    return render(request, "art.html")