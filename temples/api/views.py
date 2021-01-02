from rest_framework import generics
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission
from rest_framework.permissions import SAFE_METHODS
from core.models import City, Country, Church
from .serializers import CitySerializer, CountrySerializer, ChurchSerializer


class OwnerWritePermissions(BasePermission):
    message = 'You are not an owner of this page'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions, ]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ChurchListView(generics.ListCreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer


class ChurchDetailView(generics.RetrieveUpdateDestroyAPIView, OwnerWritePermissions):
    permission_classes = [OwnerWritePermissions, ]
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
