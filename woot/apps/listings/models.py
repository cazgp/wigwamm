from django.db import models

from libs.models import UUIDModel
from libs.fields import OneCharChoiceField
from listings.helpers import *

class Listing(UUIDModel):
    address          = models.CharField(max_length=100)
    floor            = models.CharField(choices=FLOORS, max_length=2)
    lift             = models.BooleanField()
    bedrooms         = models.PositiveIntegerField()
    price            = models.PositiveIntegerField()
    move_in_date     = models.DateField()
    kitchen_type     = OneCharChoiceField(choices=KITCHEN_TYPES)
    front_garden     = models.BooleanField()
    back_garden      = models.BooleanField()
    parking          = OneCharChoiceField(choices=PARKING_TYPES)
    pets             = models.BooleanField()
    heating          = OneCharChoiceField(choices=HEATING_TYPES)
    glazing_type     = OneCharChoiceField(choices=GLAZING_TYPES)
    glazing_material = OneCharChoiceField(choices=GLAZING_MATERIAL)
    last_decorated   = OneCharChoiceField(choices=LAST_MONTHS)
    last_refurbished = OneCharChoiceField(choices=LAST_MONTHS)
    deposit          = OneCharChoiceField(choices=DEPOSIT)
    bills_included   = models.BooleanField()
    council_tax      = OneCharChoiceField(choices=COUNCIL_TAX)
    extra_fees       = models.PositiveIntegerField()
    managed_by       = OneCharChoiceField(choices=MANAGED_BY)
    epc              = models.PositiveIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')

class ListingPhoto(models.Model):
    photo   = models.ImageField(upload_to='photos')
    listing = models.ForeignKey(Listing)
