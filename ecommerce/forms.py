#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'id': 'nombre_completo',
                                    'placeholder':'Nombre'
                                    }
                                )
                            )
    email = forms.EmailField(
        widget=forms.EmailInput(
                                attrs={
                                    'class':'form-control',
                                    'id': 'email',
                                    'placeholder':'Email'
                                    }
                                )
                            )
    comentarios = forms.CharField(
        widget=forms.Textarea(
                                attrs={
                                    'class':'form-control',
                                    'id': 'comentarios',
                                    'placeholder':'Escribe aqui, tus comentarios',
                                    'rows':'4'
                                    }
                                )
                            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Ingrese un email válido")
        return email


class LoginForm(forms.Form):
    usuario = forms.CharField(
            widget=forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'id': 'usuario',
                                'placeholder':'Usuario'
                                }
                            )
                        )
    password = forms.CharField(label='Contraseña',
            widget=forms.PasswordInput(
                            attrs={
                                'class':'form-control',
                                'id': 'password',
                                'placeholder':'Contraseña'
                                }
                            )
                        )

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id': 'usuario','placeholder':'Nuevo Usuario'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
                                attrs={
                                    'class':'form-control',
                                    'id': 'email',
                                    'placeholder':'Nuevo Email'
                                    }
                                )
                            )
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','id': 'password','placeholder':'Nueva Contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','id': 'password','placeholder':'Confirmar Contraseña'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("¡El usuario ya existe!")
        return username
    def clean(self):
        datos = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Las contraseñas no coinciden, ¡Intente Nuevamente!")
        return datos
