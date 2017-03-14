from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.pindrop.factories import PinFactory, AddressFactory
import collections


class PinDropTestCase(TestCase):

    def test_updating_status_to_middle(self):
        address = AddressFactory()
        address.save()
        pindrop = PinFactory(address=address, created=(timezone.now() - timedelta(days=8)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.MIDDLE)

    def test_updating_status_to_old(self):
        address = AddressFactory()
        address.save()
        pindrop = PinFactory(address=address, created=(timezone.now() - timedelta(days=15)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.OLD)

    def test_updating_status_to_cancelled(self):
        address = AddressFactory()
        address.save()
        pindrop = PinFactory(address=address, created=(timezone.now() - timedelta(days=22)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.REMOVED)


class AddGeocoordinatesTestCast(TestCase):
    def test_returning_latitude_and_longditude(self):

        address = collections.namedtuple(
            'address',
            ['street', 'state', 'postal_code', 'googleLat', 'googleLon']
        )
        address_book = [
            address('2 Dunbar Ave', 'VIC', 3161, -37.878505, 145.019607),
            address('19 Dunbar Ave', 'VIC', 3161, -37.878945, 145.021097),
            address('15 St kilda Rd', 'VIC', 3004, -37.818164, 144.967869)
        ]

        # Set decimal accuracy of the GPS coordinates
        accuracy = 2 
        for i in address_book:
            pindrop = AddressFactory(
                street=i.street,
                state=i.state,
                postal_code=i.postal_code
            )
            pindrop.add_geocoordinates()
            round_pin = (round(pindrop.latitude, accuracy), round(pindrop.longitude, accuracy))
            round_google = (round(i.googleLat, accuracy), round(i.googleLon, accuracy))
            self.assertEqual(round_pin, round_google)
