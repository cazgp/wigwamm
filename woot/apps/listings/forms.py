from datetime import date

from django import forms

from libs.helpers import weeks_range
from listings.models import Listing

class ListingsForm(forms.ModelForm):
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
        today = date.today()
