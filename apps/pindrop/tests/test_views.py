from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.pindrop.factories import PinFactory, ItemFactory


class PinViewTestCase(TestCase):
    """
    Tests the pin view api
    """
    def get_url(self):
        return '/api/v1/pins/'

    def test_pins_api(self):
        self.pin = PinFactory().save()
        self.item1 = ItemFactory().save()
        self.item2 = ItemFactory(name='Record Player', pin=self.pin).save()
        self.item3 = ItemFactory(name='Computer', pin=self.pin).save()
        response = self.client.get(self.get_url())
        print(response)

        # TODO: fix my pycharm dev environmet
        # TODO: see why response isn't return with any content


