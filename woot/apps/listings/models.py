from django.core.urlresolvers import reverse
from django.db import models

from libs.models import UUIDModel
from listings.helpers import *

class Listing(UUIDModel):
    address               = models.CharField(max_length=100)
    list_on               = models.CharField(
        max_length=1,
        choices=LIST_CHOICES,
    )
    floor                 = models.CharField(choices=FLOORS, max_length=2)
    lift                  = models.BooleanField()
    bedrooms              = models.CharField(max_length=2)
    bathrooms             = models.CharField(max_length=2)
    price                 = models.CharField(max_length=255)
    move_in_date          = models.DateField()
    kitchen               = models.CharField(
        max_length=1,
        choices=KITCHEN_TYPES,
    )
    front_garden = models.CharField(
        max_length=1,
        choices=FRONT_GARDEN_TYPES,
    )
    back_garden = models.CharField(
        max_length=1,
        choices=BACK_GARDEN_TYPES,
    )
    on_street_parking = models.CharField(
        max_length=1,
        choices=ON_PARKING_TYPES,
    )
    off_street_parking = models.CharField(
        max_length=1,
        choices=OFF_PARKING_TYPES,
    )
    pets = models.CharField(
        max_length=1,
        choices=PET_TYPES,
    )
    heating = models.CharField(
        max_length=1,
        choices=HEATING_TYPES,
    )
    glazing_type = models.CharField(
        max_length=1,
        choices=GLAZING_TYPES,
    )
    glazing_material = models.CharField(
        max_length=1,
        choices=GLAZING_MATERIAL,
    )
    furnished             = models.BooleanField()
    last_decorated = models.CharField(
        max_length=1,
        choices=LAST_MONTHS,
    )
    last_refurbished = models.CharField(
        max_length=1,
        choices=LAST_MONTHS,
    )
    deposit = models.CharField(
        max_length=1,
        choices=DEPOSIT,
    )
    agreement_term = models.CharField(
        max_length=1,
        choices=AGREEMENT,
    )
    water_bills_included  = models.BooleanField()
    council_tax_included  = models.BooleanField()
    energy_bills_included = models.BooleanField()
    bills_included        = models.BooleanField()
    telephone_included    = models.BooleanField()
    broadband = models.CharField(
        max_length=1,
        choices=BROADBAND,
    )
    council_borough       = models.CharField(max_length=255)
    council_tax_band = models.CharField(
        max_length=1,
        choices=COUNCIL_TAX,
    )
    agent_fee             = models.CharField(
        max_length=255,
        verbose_name='Letting agent extra fees',
    )
    managed_by = models.CharField(
        max_length=1,
        choices=MANAGED_BY,
    )
    epc_code              = models.CharField(blank=True, null=True,
                                             max_length=10)

    def get_absolute_url(self):
        return reverse('home')

class ListingPhoto(models.Model):
    photo   = models.ImageField(upload_to='photos')
    listing = models.ForeignKey(Listing)
