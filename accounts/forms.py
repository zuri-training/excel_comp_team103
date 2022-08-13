from django.db import models
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
    



