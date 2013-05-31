from django.db import models

from libs.models import UUIDModel
from libs.fields import OneCharChoiceField
from listings.helpers import *

class Listing(UUIDModel):
    address               = models.CharField(max_length=100)
    floor                 = models.CharField(choices=FLOORS, max_length=2)
    lift                  = models.BooleanField()
    bedrooms              = models.PositiveIntegerField()
    price                 = models.PositiveIntegerField()
    move_in_date          = models.DateField()
    kitchen               = OneCharChoiceField(choices=KITCHEN_TYPES)
    front_garden          = OneCharChoiceField(choices=FRONT_GARDEN_TYPES)
    back_garden           = OneCharChoiceField(choices=BACK_GARDEN_TYPES)
    on_street_parking     = OneCharChoiceField(choices=ON_PARKING_TYPES)
    off_street_parking    = OneCharChoiceField(choices=OFF_PARKING_TYPES)
    pets                  = OneCharChoiceField(choices=PET_TYPES)
    heating               = OneCharChoiceField(choices=HEATING_TYPES)
    glazing_type          = OneCharChoiceField(choices=GLAZING_TYPES)
    glazing_material      = OneCharChoiceField(choices=GLAZING_MATERIAL)
    furnished             = models.BooleanField()
    last_decorated        = OneCharChoiceField(choices=LAST_MONTHS)
    last_refurbished      = OneCharChoiceField(choices=LAST_MONTHS)
    deposit               = OneCharChoiceField(choices=DEPOSIT)
    agreement_term        = OneCharChoiceField(choices=AGREEMENT)
    water_bills_included  = models.BooleanField()
    council_tax_included  = models.BooleanField()
    energy_bills_included = models.BooleanField()
    bills_included        = models.BooleanField()
    telephone_included    = models.BooleanField()
    broadband             = OneCharChoiceField(choices=BROADBAND)
    council_borough       = models.CharField(max_length=255)
    council_tax           = OneCharChoiceField(choices=COUNCIL_TAX)
    extra_fees            = models.PositiveIntegerField()
    managed_by            = OneCharChoiceField(choices=MANAGED_BY)
    epc                   = models.PositiveIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')

class ListingPhoto(models.Model):
    photo   = models.ImageField(upload_to='photos')
    listing = models.ForeignKey(Listing)
