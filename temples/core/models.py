from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from users.models import CustomUser
from .choices import SEASONS, ALL_SEASONS


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    """
    Local name of groups of districts
    """
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    address_str = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, null=True)
    country = models.ForeignKey(Country,
                                on_delete=models.deletion.SET_NULL,
                                null=True)
    city = models.ForeignKey(City,
                             on_delete=models.deletion.SET_NULL,
                             null=True)
    district = models.ForeignKey(District,
                                 on_delete=models.deletion.SET_NULL,
                                 null=True)
    street = models.ForeignKey(Street,
                               on_delete=models.deletion.SET_NULL,
                               null=True)
    house = models.CharField(max_length=20, null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return self.slug


class Church(models.Model):

    class PublishedObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=500, null=False)
    slug = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    author = models.ForeignKey(CustomUser,
                               on_delete=models.deletion.CASCADE,
                               null=True,
                               blank=True)
    address = models.ForeignKey(Address,
                                on_delete=models.deletion.SET_NULL,
                                null=True)
    path_to_go = models.TextField()
    social_link = models.URLField()
    site_link = models.URLField()
    main_order = models.IntegerField(null=False,
                                     validators=[MinValueValidator(0),
                                                 MaxValueValidator(200)]
                                     )
    status = models.CharField(max_length=9, choices=options, default='draft')
    objects = models.Manager()
    published_objects = PublishedObjects()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('object_detail', args=[self.slug])

    class Meta:
        ordering = ('main_order',)


class Tag(models.Model):
    class Meta:
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50)
    church = models.ManyToManyField(Church)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    church = models.ForeignKey(Church, on_delete=models.deletion.CASCADE)
    is_in_list = models.BooleanField(default=False)
    season = models.CharField(
        max_length=100,
        choices=SEASONS,
        default=ALL_SEASONS,
        verbose_name=_('Season when this photo is created'),
        null=True
    )
    tip_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Audio future
#
#
# class Video
#
#
class Comment(models.Model):
    object_of_comment = models.ForeignKey(Church,
                                          on_delete=models.deletion.CASCADE)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.deletion.CASCADE,
                               null=True,
                               blank=True)
    anonymous = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text
