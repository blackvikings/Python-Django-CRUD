from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactFrom, LoginFrom

def home_page(request):
    context={
        "title":"Hello World",
        "content":"Welcome to home page"
    }
    if request.user.is_authenticated:
        context={"premium_content": "YEAHHHH" }
    return render(request, "home_page.html", context)

def about_page(request):
    context={
        "title":"Hello World",
        "content":"Welcome to about page",
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactFrom(request.POST or None)
    context={
        "title": "Hello World",
        "content": "Welcome to contact us",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/views.html", context)

def login_page(request):
    form = LoginFrom(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        context['form'] = LoginFrom()
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginFrom(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})