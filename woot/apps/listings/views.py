from datetime import date

from django.views.generic import CreateView, TemplateView

from listings.forms import ListingsForm
from libs.helpers import weeks_range
from listings.models import Listing

class HomeView(TemplateView):
    template_name = 'home.html'

class ListingsView(CreateView):
    model = Listing
    form_class = ListingsForm

    def get_context_data(self, **kwargs):
        context = super(ListingsView, self).get_context_data(**kwargs)
        today = date.today()
        context['move_in_dates'] = weeks_range(today, 12)
        context['today'] = today
        keypad_num = range(1, 10)
        keypad_num.extend(['decimal', 0, 'backspace'])
        keypad_grid = range(1, 24, 2)
        keypad = zip(keypad_num, keypad_grid)
        context['keypad'] = keypad
        return context


    '''
    def form_valid(self, form):
        # On POST success method
        form.make_listings()
        form.instance.created_by = self.request.user
        return super(ListingsView, self).form_valid(form)
'''
