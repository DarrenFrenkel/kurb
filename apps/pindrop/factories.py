imporimport random

import factory
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.pindrop import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    email = factory.Sequence(lambda n: '%s@testuser.com.au' % n)
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


# Ideally we should be using `DjangoModelFactory`
# However, when using `DjangoModelFactory` I'm not able to custom generate a `created` field
# Therefore I went the Factory subclass and create a random pk/id
class PinFactory(factory.Factory):

    class Meta:
        model = models.Pin

    user = factory.SubFactory(UserFactory)
    address_street = factory.Sequence(lambda n: '{} test street{}'.format(n, n))
    address_city = 'Melbourne'
    address_postal_code = random.randint(1000, 9999)
    latitude = Decimal(random.random())
    longitude = Decimal(random.random())
    created = timezone.now()
    pk = random.randint(1, 10000000)



class ItemFactory(factory.Factory):

    class Meta:
        model = models.Item

    name = 'Television'
    category = models.Item.CATEGORY.ELECTRONICS
    condition = models.Item.CONDITION.BRAND_NEW
    pin = factory.SubFactory(PinFactory)
