from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Group, Messages, Subject, User

# Create your views here.


def home(request):
    context = {}
    return render(request, 'groupOn/home.html', context)
