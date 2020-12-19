from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django import forms
from .models import Church, City, Country, Address, Tag, District, Street, Comment


class CustomChurch(admin.ModelAdmin):
    list_display = ("main_order", "name", "slug", "short_description")
    search_fields = ("short_description__contains",
                     "name__contains", "slug__contains", )


admin.site.register(Church, CustomChurch)


class CustomCity(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Name of City or small town in agglomeration:"
        return form


admin.site.register(City, CustomCity)


class CustomCountry(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Country, CustomCountry)


class CustomAddress(admin.ModelAdmin):
    list_display = ("address_str", "city", "district")
    list_filter = ("city", )


admin.site.register(Address, CustomAddress)


class CustomDistrict(admin.ModelAdmin):
    list_display = ("name", "slug", "list_churches")

    def list_churches(self, obj):
        count = obj.address_set.count()
        url = (
                reverse("admin:core_address_changelist")
                + "?"
                + urlencode({"district__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} object(s)</a>', url, count)

    list_churches.short_description = "Churches"


admin.site.register(District, CustomDistrict)


class CustomStreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = "__all__"

    def clean_name(self):
        if self.cleaned_data["name"].startswith('ул'):
            raise forms.ValidationError("Enter only street name")

        return self.cleaned_data["name"]


class CustomStreet(admin.ModelAdmin):
    form = CustomStreetForm


admin.site.register(Street, CustomStreet)


class CustomTag(admin.ModelAdmin):
    list_display = ("name_tag", "count_churches")

    def name_tag(self, obj):
        result = obj.name
        return format_html("<b><i>{}</i></b>", result)

    def count_churches(self, obj):
        count = Church.objects.filter(tag=obj).count()
        return count

    count_churches.short_description = "Сhurch count"


admin.site.register(Tag, CustomTag)
admin.site.register(Comment)


# def update_premiere(book):
#     """Pretend to update the book to be a premiere.
#
#     This function is to make the demo clear.
#     In a real application, this could be a manager method instead
#     which would update the book and trigger the email notifications
#     (e.g., `Book.objects.update_premiere(book)`).
#     """
#     print(f"Update {book.title} state to change premiere books.")
#     print("Call some background task to notify interested users via email.")

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     actions = ["set_premiere"]
#     date_hierarchy = "published_date"
#     inlines = [ReviewInline]
#     list_display = ("id", "title")
#     list_filter = ("category",)
#     ordering = ("title",)
#     raw_id_fields = ("editor",)
#     prepopulated_fields = {"slug": ("title",)}
#     search_fields = ("author",)
#
#     def set_premiere(self, request, queryset):
#         if len(queryset) == 1:
#             book = queryset[0]
#             update_premiere(book)