from django.contrib import admin

# Register your models here.
from apps.pindrop.models import Pin, Item

admin.site.register(Pin)
admin.site.register(Item)
