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
    if isinstance(field, OneCharChoiceField):
        return field.formfield(
            widget=forms.RadioSelect(
                attrs={'id': field.name}
            )
        )
    return field.formfield()

class ListingForm(forms.ModelForm):
    formfield_callback = make_formfield
    listing_destination = forms.MultipleChoiceField(
        choices=[
            ('r', 'rightmove'),
            ('z', 'zoopla'),
            ('g', 'gumtree'),
            ('c', 'craig\'s list'),
        ],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Listing

ListingPhotoFormSet = inlineformset_factory(
    Listing, ListingPhoto, extra=19, can_delete=False)
