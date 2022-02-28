from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import fUserCreate, fCreatePost
from .models import mCreatePost
# Create your views here.

def index(request):
    posts = mCreatePost.objects.all()
    if request.user.is_authenticated:
          return render(request, "index.html", {
              "posts": posts
          })
    else:
        return HttpResponseRedirect(reverse("blog:sign_in"))
def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("blog:index"))
    if request.method == "POST":  
        username = request.POST["username"]
        password = request.POST["password"]
        user_login = authenticate(username = username, password=password)
        if user_login is not None:
            login(request, user_login)
            return render(request, "index.html")
        else:
            return render(request, "pages/sign-in.html", {
                "message": "Your account is incorrect!" 
            })
    return render(request, "pages/sign-in.html")

def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse("blog:index"))
    return HttpResponseRedirect(reverse("blog:index"))
def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse("blog:sign_out"))
    if request.method == "POST":
        form = fUserCreate(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            new_user = authenticate(username=username, password = password)
            if new_user is not None:
                login(request, new_user)
                return HttpResponseRedirect(reverse("blog:index"))
        return render(request, "pages/sign-up.html", {
            "form": form
        })
    return render(request, "pages/sign-up.html", {
        "form": fUserCreate()
    })
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, "pages/profile.html")
    return HttpResponseRedirect(reverse("blog:sign_in"))
def post_create(request):
    if request.method == "POST":
        form = fCreatePost(request.POST)
        if form.is_valid():
            saveForm = mCreatePost(title = form.cleaned_data["title"], description = form.cleaned_data["description"], body = form.cleaned_data["body"])
            saveForm.author = request.user
            saveForm.save()
            return HttpResponseRedirect(reverse("blog:index"))
        return render(request, "pages/createpost.html", {
            "form": form
        })
    return render(request, "pages/createpost.html", {
        "form": fCreatePost()
    })