from django.db import models
from libs.models import UUIDModel
from libs.fields import OneCharChoiceField
from photologue.models import Photo

KITCHEN_TYPES = (
    (1, 'Open-plan'),
    (2, 'Separate'),
)

PARKING_TYPES = (
    (1, 'garage'),
    (2, 'double'),
    (3, 'single'),
)

HEATING_TYPES = (
    (1, 'gas'),
    (2, 'oil'),
    (3, 'electric'),
)

GLAZING_TYPES = (
    (1, 'single'),
    (2, 'double'),
    (3, 'triple'),
)

GLAZING_MATERIAL = (
    (1, 'timer'),
    (2, 'UPVC'),
)

LAST_MONTHS = (
    (1, '1 month'),
    (2, '12 months'),
    (3, '24 months'),
)

DEPOSIT = (
    (1, '1 month'),
    (2, '6 weeks'),
    (3, '2 months'),
)

COUNCIL_TAX = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E'),
    (6, 'F'),
    (7, 'G'),
)

MANAGED_BY = (
    (1, 'agent'),
    (2, 'landlord'),
)

class Listing(UUIDModel):
    address          = models.CharField(max_length=100)
    floor            = models.PositiveIntegerField()
    lift             = models.BooleanField()
    bedrooms         = models.PositiveIntegerField()
    price            = models.PositiveIntegerField()
    move_in_date     = models.DateField()
    photos           = models.ManyToManyField(Photo)
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
