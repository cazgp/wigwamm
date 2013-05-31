from datetime import date

from django import forms
from django.db import models
from django.forms.models import inlineformset_factory

from libs.fields import OneCharChoiceField
from libs.helpers import weeks_range
from listings.models import Listing, ListingPhoto

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]

bool_choices = (
    (1, 'Yes'),
    (0, 'No'),
)

def make_formfield(field, *args, **kwargs):
    if isinstance(field, models.BooleanField):
        return forms.TypedChoiceField(
            coerce=bool, choices=bool_choices,
            widget=forms.RadioSelect(
                attrs={'id': field.name}
            )
        )
    if isinstance(field, models.CharField):
        if field.max_length == 1 or field.name == 'floor':
            return field.formfield(
                widget=forms.RadioSelect(
                    attrs={'id': field.name}
                )
            )
    return field.formfield()

class ListingForm(forms.ModelForm):
    formfield_callback = make_formfield

    class Meta:
        model = Listing
        fields = ['address', 'list_on', 'move_in_date', 'price',
                  'bedrooms', 'bathrooms', 'floor', 'lift', 'kitchen',
                  'front_garden', 'back_garden', 'on_street_parking',
                  'off_street_parking', 'pets', 'heating', 'glazing_type',
                  'glazing_material', 'furnished', 'last_decorated',
                  'last_refurbished', 'deposit', 'agreement_term',
                  'water_bills_included', 'council_tax_included',
                  'energy_bills_included', 'telephone_included', 'broadband',
                  'council_borough', 'council_tax_band', 'agent_fee',
                  'managed_by', 'epc_code']

ListingPhotoFormSet = inlineformset_factory(
    Listing, ListingPhoto, extra=19, can_delete=False)
