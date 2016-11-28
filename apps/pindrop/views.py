from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.pindrop.models import Pin
from apps.pindrop.serializers import PinSerializer


class PinViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer

    def get_object(self):
        obj = super(PinViewSet, self).get_object()
