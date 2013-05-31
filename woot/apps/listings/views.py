from datetime import date

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from libs.helpers import weeks_range

from listings.forms import ListingForm, ListingPhotoFormSet
from listings.helpers import photo_order
from listings.models import Listing, ListingPhoto

class HomeView(TemplateView):
    template_name = 'home.html'

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]

class ListingView(CreateView):
    model = Listing
    form_class = ListingForm

    def get_context_data(self, **kwargs):
        context = super(ListingView, self).get_context_data(**kwargs)
        today = date.today()
        context['move_in_dates'] = weeks_range(today, 12)
        context['today'] = today
        keypad_num = range(1, 10)
        keypad_num.extend(['decimal', 0, 'backspace'])
        keypad_grid = range(1, 24, 2)
        keypad = zip(keypad_num, keypad_grid)
        context['keypad'] = keypad

        if self.request.method == 'POST':
            listingphoto_form = ListingPhotoFormSet(self.request.POST,
                                                    self.request.FILES)

        else:
            listingphoto_form = ListingPhotoFormSet()

        context['listingphoto_form'] = listingphoto_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        listingphoto_form = context['listingphoto_form']
        if listingphoto_form.is_valid():
            self.object = form.save()
            listingphoto_form.instance = self.object
            listingphoto_form.save()
            return HttpResponseRedirect('/created/')
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
