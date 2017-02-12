from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.pindrop.factories import PinFactory
import collections

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
      
        address = collections.namedtuple('address', ['address_street','address_city', 'address_postal_code', 'googleLat', 'googleLon'] )
        addressBook = [address('2 Dunbar Ave','Melbourne', 3161, -37.878505, 145.019607),
                       address('19 Dunbar Ave','Melbourne', 3161, -37.878945, 145.021097),
                       address('15 Stkilda Rd', 'Melbourne', 3004, -37.818164, 144.967869) ]
        
        #Set decimal accuracy of the GPS coordinates
        accuracy = 2 
        for i in addressBook:
            pindrop = PinFactory(address_street=i.address_street, address_city=i.address_city, address_postal_code=i.address_postal_code)
            pindrop.add_geocoordinates() 
            rndPinLatLon = (round(pindrop.latitude, accuracy) , round(pindrop.longitude, accuracy))
            rndGoogleLatLon = (round(i.googleLat, accuracy), round(i.googleLon, accuracy))
            self.assertEqual(rndPinLatLon, rndGoogleLatLon)
        




