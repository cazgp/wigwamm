from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.dispatch

from libs.models import UUIDModel
from listings.helpers import *
from listings.sites import create_rightmove

class Listing(UUIDModel):
    address_1             = models.CharField(max_length=100)
    address_2             = models.CharField(max_length=100,
                                             blank=True,
                                             null=True)
    town = models.CharField(max_length=100)
    postcode              = models.CharField(max_length=8)
    property_type         = models.CharField(
        max_length=1,
        choices=PROPERTY_TYPES,
    )
    #list_on               = models.CharField(
        #max_length=1,
        #choices=LIST_CHOICES,
    #)
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

# Saves user login details for sites
class ListingSite(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    site = models.CharField(max_length=1, default=0)
    listing = models.ForeignKey(Listing)

# Signal for when the listing has been uploaded
listing_done = django.dispatch.Signal(providing_args=['instance'])

@receiver(listing_done, dispatch_uid="listing-created")
def listing_handler(sender, **kwargs):
    create_rightmove(kwargs['instance'])
