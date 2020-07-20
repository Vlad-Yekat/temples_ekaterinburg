from django.db import models


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
    country = models.ForeignKey(Country, on_delete=models.deletion.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.deletion.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.deletion.SET_NULL, null=True)
    street = models.ForeignKey(Street, on_delete=models.deletion.SET_NULL, null=True)
    house = models.CharField(max_length=20, null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return self.slug


class Church(models.Model):
    name = models.CharField(max_length=500, null=False)
    slug = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.deletion.SET_NULL, null=True)
    path_to_go = models.TextField()
    social_link = models.URLField()
    site_link = models.URLField()
    main_order = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    church = models.ManyToManyField(Church)

    def __str__(self):
        return self.name


# class Image(models.Model): future
#
#
# class Audio
#
#
# class Video
#
#
# class Comment