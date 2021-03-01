from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'OmarS',
        'title': 'Post 1',
        'content': 'Content',
        'date_posted': 'Today'
    },
    {
        'author': 'John Doe',
        'title': 'Post 2',
        'content': 'Content2',
        'date_posted': 'Tomorrow'
    }
]

def home(request):
    return render(request, 'translate/home.html')

def sign_up(request):
    return render(request, 'translate/signup.html', {'title': 'Signup'})

def view_messages(request):
    context = {
        'posts': posts
    }
    return render(request, 'translate/messages.html', context)
