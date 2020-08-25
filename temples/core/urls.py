"""
django urls for core app
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import MainListView, ObjectDetailView

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('<str:slug>/', ObjectDetailView.as_view(), name='object_detail'),
]


urlpatterns += staticfiles_urlpatterns()
