from rest_framework import serializers

from apps.pindrop.models import Pin, Item, Address


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'name',
            'category',
            'condition'
        )


class PinSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = (
            'pk',
            'status',
            'items'
        )


class AddressSerializer(serializers.ModelSerializer):
    pins = PinSerializer(many=True, read_only=True)

    class Meta:
        model = Address
        fields = (
            'pk'
            'street',
            'state',
            'postal_code'
            'latitude'
            'longitude')
