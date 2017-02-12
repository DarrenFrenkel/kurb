from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.pindrop.factories import PinFactory


class PinDropTestCase(TestCase):

    def test_updating_status_to_middle(self):
        pindrop = PinFactory(created=(timezone.now() - timedelta(days=8)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.MIDDLE)

    def test_updating_status_to_old(self):
        pindrop = PinFactory(created=(timezone.now() - timedelta(days=15)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.OLD)

    def test_updating_status_to_cancelled(self):
        pindrop = PinFactory(created=(timezone.now() - timedelta(days=22)))

        self.assertEqual(pindrop.status, pindrop.STATE.NEW)
        pindrop.update_status()
        self.assertEqual(pindrop.status, pindrop.STATE.REMOVED)

class Add_GeocoordinatesTestCast(TestCase):
    def test_returning_latitude_and_longditude(self):
        pindrop0 = PinFactory(address_street='19 Dunbar Ave', address_city='Melbourne', address_postal_code=3161)
        pindrop0.add_geocoordinates()
        self.assertEqual(pindrop0.longitude, 145.019581)
        




