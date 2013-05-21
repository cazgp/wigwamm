from django.forms.models import ModelForm

from listings.models import Listing

class ListingsForm(ModelForm):
    def make_listings(self):
        pass

    class Meta:
        model = Listing
