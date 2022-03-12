from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

from django.contrib import messages

from .models import Profile, Post
from .forms import UserRegisterForm, PostForm


@login_required
def home(request):
    posts = Post.objects.all()
    # New twit
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # aqui si se necesita agregar que usuario hace el post
            post = form.save(commit=False)
            post.profile = request.user.profile
            post.save()
            return redirect('home')
    else:
        form = PostForm
    ctx = {"posts": posts, "form":form}

    return render(request, 'users/home.html', ctx)


@login_required
def view_user(request, profile):
    current_profile = get_object_or_404(Profile, user__username=profile)
    posts = Post.objects.all().filter(profile=current_profile)

    ctx = {"current_profile": current_profile, "posts": posts}
    return render(request, 'users/view_user.html', ctx)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, "users/register.html", context)
