from rest_framework import serializers

from apps.pindrop.models import Pin, Item


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
            'address_street',
            'address_number',
            'address_city',
            'address_postal_code',
            'status',
            'items'
        )
