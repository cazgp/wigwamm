from datetime import date

from django import forms
from django.forms.models import inlineformset_factory

from libs.helpers import weeks_range
from listings.models import Listing, ListingPhoto

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]

class ListingForm(forms.ModelForm):
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
        widgets = {
            'floor': forms.RadioSelect(
                attrs={'id': 'floor'}
            )
        }

ListingPhotoFormSet = inlineformset_factory(
    Listing, ListingPhoto, extra=19, can_delete=False)
