from django.views.generic import CreateView

from listings.forms import ListingsForm
from listings.models import Listing

class ListingsView(CreateView):
    model = Listing
    #form_class = ListingsForm

    '''
    def form_valid(self, form):
        # On POST success method
        form.make_listings()
        form.instance.created_by = self.request.user
        return super(ListingsView, self).form_valid(form)
'''
