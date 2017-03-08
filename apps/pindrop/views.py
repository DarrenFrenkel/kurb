import json
import os

from django.forms.models import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from rest_framework import viewsets

from apps.pindrop.models import Pin, Item, Address
from apps.pindrop.serializers import PinSerializer


class PinViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer

    def get_object(self):
        obj = super(PinViewSet, self).get_object()


class PinView(ListView):
    """
    A list of pins and associated items
    """
    model = Pin
    template_name = "pin/pin.html"

    def get_context_data(self, **kwargs):
        pins = list()
        # Create a list of pin dicts that include the pins related items
        for pin in self.model.objects.all():
            pin_dict = model_to_dict(pin)
            items = [{'name': item.name, 'category': item.category, 'condition': item.condition}
                     for item in pin.items.all()]
            pin_dict['items'] = items
            address = {
                'street': pin.address.street,
                'state': pin.address.state,
                'postal_code': pin.address.postal_code,
                'latitude': pin.address.latitude,
                'longitude': pin.address.longitude
            }
            pin_dict['address'] = address
            pins.append(pin_dict)
        kwargs['pins'] = json.dumps(pins)
        kwargs['google_key'] = os.environ['google_key']
        return super(PinView, self).get_context_data(**kwargs)
