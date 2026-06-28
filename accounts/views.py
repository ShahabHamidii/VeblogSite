from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, EditProfileForm



def my_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {'form': form})

def my_logout(request):
    logout(request)
    return redirect('home_app:home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    context = {'errors':[]}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password != password2:
            context['errors'].append("Passwords don't match")
            return render(request, 'accounts/signup.html', context)
        if username is None or username == '':
            context['errors'].append("Username is required")
            return render(request, 'accounts/signup.html', context)
        if email is None or email == '':
            context['errors'].append("Email is required")
            return render(request, 'accounts/signup.html', context)
        if User.objects.filter(username=username).exists():
            context['errors'].append("Username already exists")
            return render(request, 'accounts/signup.html', context)

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request,user)
        return redirect('home_app:home')
    return render(request, "accounts/signup.html")

def edit_profile(request):
    user = request.user
    form = EditProfileForm(instance=user)
    if request.method == "POST":
        form = EditProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/edit.html', {'form': form})

