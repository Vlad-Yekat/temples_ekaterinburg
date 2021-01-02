"""
django urls for core app
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import CityListView, CityDetailView, CountryListView, ChurchListView, ChurchDetailView

app_name = 'api'

urlpatterns = [
    path('city/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('city/', CityListView.as_view(), name='city_index'),
    path('country/', CountryListView.as_view(), name='country_index'),
    path('church/<int:pk>/', ChurchDetailView.as_view(), name='church_detail'),
    path('church/', ChurchListView.as_view(), name='church_index'),
]

