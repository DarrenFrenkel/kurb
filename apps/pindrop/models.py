from __future__ import unicode_literals
from geopy.geocoders import Nominatim

import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.pindrop.utils import ChoicesList


class Pin(models.Model):
    """
    A model that represents the location where you place stuff on the nature strip
    """
    STATE = ChoicesList(
        # Post is new
        ('new', 'New'),
        # Post is middle aged
        ('middle', 'Middle'),
        # Post is old
        ('old', 'Old'),
        # Post is old enough to remove
        ('removed', 'Removed'),
        # Item was picked up
        ('picked up', 'Picked Up'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='pins')
    address_street = models.CharField(max_length=255)
    address_number = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_postal_code = models.CharField(max_length=255)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    created = models.DateTimeField("created time", auto_now_add=True)
    updated = models.DateTimeField("updated time", auto_now=True)
    status = models.CharField(max_length=32, choices=STATE, default=STATE.NEW)

    def update_status(self):
        """
        Updates the pins status to middle, old or removed
        :return: The instance it's updating
        """
        if self.created.date() < timezone.now().date() - datetime.timedelta(days=21):
            self.status = self.STATE.REMOVED
            self.save()
        elif self.created.date() < timezone.now().date() - datetime.timedelta(days=14):
            self.status = self.STATE.OLD
            self.save()
        elif self.created.date() < timezone.now().date() - datetime.timedelta(days=7):
            self.status = self.STATE.MIDDLE
            self.save()
        return self

    def add_geocoordinates(self):
        geolocator = Nominatim()
        location = geolocator.geocode('{}, {} {}'.format(
            self.address_street, self.address_city, self.address_state
        ))
        self.latitude = location.latitude
        self.longitude = location.longitude

    def __str__(self):
        return '{} {}, {}'.format(self.address_number, self.address_street, self.address_postal_code)


class Item(models.Model):
    """
    A model that represents the items that you are placing on the nature strip
    """
    CATEGORY = ChoicesList(
        ('furniture', 'Furniture'),
        ('electronics', 'Electronics'),
        ('television', 'Television'),
        ('computer', 'Computer'),
        ('appliances', 'Appliances'),
    )

    CONDITION = ChoicesList(
        ('brand new', 'Brand New'),
        ('like new', 'Like New'),
        ('very good', 'Very Good'),
        ('good', 'Good'),
        ('acceptable', 'Acceptable'),
    )

    name = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=32, choices=CATEGORY, blank=True)
    condition = models.CharField(max_length=32, choices=CONDITION, blank=True)
    pin = models.ForeignKey('Pin', related_name='items', blank=True, null=True)

    def __str__(self):
        return '{} - <{}>'.format(self.name, self.category)

# TODO: start thinking how are we going to create an end point - (use btool as an example)
# TODO: At some point we have to thinnk about how are we are going to call update_status (via celery or cron job). Note that we should exclude status=cancel when calling update_status
