from django.contrib import admin

# Register your models here.
from apps.pindrop.models import Address, Pin, Item

admin.site.register(Address)
admin.site.register(Pin)
admin.site.register(Item)
