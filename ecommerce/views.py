#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactoForm, LoginForm, RegisterForm
User = get_user_model()
def home_page(request):
    usuario = User
    context = {
        "title":"Inicio",
        "content": "Welcome to home page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    form = ContactoForm(request.POST or None)
    context = {
        "title":"Contacto",
        "content": "Welcome to contact page",
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"Acerca de",
        "content": "Welcome to about page"
    }
    return render(request, "home_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("usuario")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # context['form'] = LoginForm()
            return redirect("/")
            print(request.user.is_authenticated())
        else:
            print("error")
    return render(request, "auth/login.html",context)



def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        usuario_nuevo = User.objects.create_user(username,email,password)
        messages.info(request, '¡Usuario Registrado Exitosamente!')
        print(usuario_nuevo)
    return render(request, "auth/register.html",context)
