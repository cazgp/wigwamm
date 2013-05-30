from django import template
from django.shortcuts import render_to_response

from listings.helpers import photo_order

register = template.Library()

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]

@register.inclusion_tag('listings/photo_form.html')
def label_photo(field):
    number = int(field.html_name.split('-')[1])
    room = photo_order[number]
    label = room.replace('-', ' ')
    return {
        'room': room,
        'id': field.auto_id,
        'room_label': label,
    }
