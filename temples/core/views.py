from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Church


class MainListView(ListView):
    model = Church

    template_name = 'core/index.html'
