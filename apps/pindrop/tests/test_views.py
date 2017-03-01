from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.pindrop.factories import PinFactory, ItemFactory, AddressFactory


class PinViewTestCase(TestCase):
    """
    Tests the pin view api
    """
    def get_url(self):
        return '/api/v1/pins/'

    def test_pins_api(self):
        self.address = AddressFactory()
        self.address.save()
        self.pin = PinFactory(address=self.address)
        self.pin.save()
        self.item1 = ItemFactory()
        self.item1.save()
        self.item2 = ItemFactory(name='Record Player', pin=self.pin)
        self.item2.save()
        self.item3 = ItemFactory(name='Computer', pin=self.pin)
        self.item3.save()
        response = self.client.get(self.get_url())
        print(response.content)

        # TODO: fix my pycharm dev environmet
        # TODO: see why response isn't return with any content

# Check pin model is working working.
class PinTestCase(TestCase):

    def get_url(self):
        return '/pin'

    def setUp(self):
        self.address = AddressFactory()
        self.address.save()
        self.pin = PinFactory(address=self.address)
        self.pin.save()
        self.item1 = ItemFactory()
        self.item1.save()
        self.item2 = ItemFactory(name='Record Player', pin=self.pin)
        self.item2.save()
        self.item3 = ItemFactory(name='Computer', pin=self.pin)
        self.item3.save()

    def test_pin_context(self):
        response = self.client.get(self.get_url())
        
        print(response.content)
