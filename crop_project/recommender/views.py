from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not phone or not password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('signup')
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('signup')
        if User.objects.filter(username=email):
            messages.error(request, 'Email is already registered.')
            return redirect('signup')
        user = User.objects.create_user(username=email, password=password)
        if " " in name:
            first, last = name.split(" ", 1)
        else:
            first, last = name, ""
        user.first_name = first
        user.last_name = last
        user.save()

        UserProfile.objects.create(user=user, phone=phone)
        login(request, user)
        messages.success(request, 'Account created successfully! You are now logged in.')
        return redirect('predict')
    return render(request, 'signup.html')

def predict_view(request):
    return render(request, 'predict.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Invalid Login Credentials.')
            return redirect('login')
        login(request, user)
        messages.success(request, 'Login successful!')
        return redirect('predict')
    return render(request, 'login.html')