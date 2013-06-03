from datetime import date

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from libs.helpers import weeks_range

from listings.forms import ListingForm, ListingPhotoFormSet, ListingSiteFormSet
from listings.helpers import photo_order
from listings.models import Listing, ListingPhoto, listing_done

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
            listingsite_form = ListingSiteFormSet(self.request.POST)

        else:
            listingphoto_form = ListingPhotoFormSet()
            listingsite_form = ListingSiteFormSet()

        context['listingphoto_form'] = listingphoto_form
        context['listingsite_form'] = listingsite_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        listingphoto_form = context['listingphoto_form']
        listingsite_form = context['listingsite_form']
        if listingphoto_form.is_valid() \
           and listingsite_form.is_valid() \
           and form.is_valid():
            self.object = form.save()
            listingphoto_form.instance = self.object
            listingphoto_form.save()
            listingsite_form.instance = self.object
            listingsite_form.save()
            listing_done.send(sender=self, instance=self.object)
            return HttpResponseRedirect('/created/')
        return self.render_to_response(self.get_context_data(form=form))
        """
        if listingphoto_form.is_valid():
            self.object = form.save()
            listingphoto_form.instance = self.object
            listingphoto_form.save()
        """
        return super(ListingView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
