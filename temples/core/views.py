from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Church


class MainListView(ListView):
    model = Church
    context_object_name = 'main_list'
    template_name = 'core/index.html'


class ObjectDetailView(DetailView):
    model = Church
    context_object_name = 'object'
    template_name = 'core/object_detail.html'
