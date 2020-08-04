from django.contrib import admin
from .models import Church, City, Country, Address, Tag, District, Street, Comment


admin.site.register(Church)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(District)
admin.site.register(Street)
admin.site.register(Tag)
admin.site.register(Comment)
