from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Comment, Genre
from .forms import CommentForm, SearchForm
import random


def genre():
    genre = Genre.objects.all()
    genre = genre[::-1]
    return genre
# Create your views here.
def index(request):
    posts = Books.objects.all()
    context = {'posts': posts, 'genre': genre()}
    form = SearchForm(request.POST)
    print(form)
    return render(request, 'main.html', context=context)


def get_post_by_category(request, id):
    post = Books.objects.filter(category_id=id)
    context = {'post': post, 'genre': genre()}
    return render(request, 'genre.html', context=context)



def book_detail(request, id):
    post = Books.objects.get(id=id)
    if request.method == "GET":
        form = CommentForm()
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
    post = Books.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    context = {
        'comments':comments, # ключ: имя переменной
        "post":post,
        "form":form,
        'genre':genre()
    }
    return render(request, "books_deteil.html", context=context)
def new_books(request):
    posts = Books.objects.all()
    posts = posts[::-1]
    context = {'posts':posts,'genre': genre()}
    return render(request, 'news.html', context=context)

def random_books(request):
    posts = list(Books.objects.all())
    shuffle_books = random.sample(posts, len(posts))
    context = {'posts':shuffle_books,'genre':genre()}
    return render(request, 'random.html', context=context)
# def search(request, name):
#     if request.method == 'GET':
#         form = SearchForm()
#     elif request.method == 'POST':
#         form = SearchForm(request.POST)
#
#     context = {'posts':posts,'genre': genre()}
#     return render(request, 'main.html', context=context)
