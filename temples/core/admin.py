from django.contrib import admin
from django.utils.html import format_html
from .models import Church, City, Country, Address, Tag, District, Street, Comment

admin.site.register(Church)
admin.site.register(City)


class CustomCountry(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Country, CustomCountry)

admin.site.register(Address)


class CustomDistrict(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(District, CustomDistrict)
admin.site.register(Street)


class CustomTag(admin.ModelAdmin):
    list_display = ("name_tag", "count_churches")

    def name_tag(self, obj):
        result = obj.name
        return format_html("<b><i>{}</i></b>", result)

    def count_churches(self, obj):
        result = Church.objects.filter(tag=obj).count()
        return result

    count_churches.short_description = "Сhurch count"


admin.site.register(Tag, CustomTag)
admin.site.register(Comment)
