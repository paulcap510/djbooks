from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def search_results(request):
    query = request.GET.get('query', '')
    books = []

    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=20"
        response = requests.get(url)
        books = response.json().get('items', [])

    return render(request, 'search_results.html', {'books': books})

def index(request):
    return render(request, 'index2.html')