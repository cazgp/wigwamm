from itertools import cycle as itertools_cycle

from django import template
from django.template.base import TemplateSyntaxError, Node
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

@register.inclusion_tag('listings/boolean_radio_form.html')
def boolean_radio(field, yes_text, no_text):
    return {
        'field': field,
        'yes': yes_text,
        'no': no_text,
    }

@register.inclusion_tag('listings/choice_radio_form.html')
def choice_radio(field):
    last_index = 35
    num_indexes = len(field.field.choices) - 2
    start_index = last_index - (num_indexes * 5)
    return {
        'field': field,
        'grid_indexes': range(start_index, last_index+1, 5)
    }

@register.inclusion_tag('listings/choice_radio_two_form.html')
def choice_radio_two(field):
    last_index = 35
    num_indexes = len(field.field.choices) - 2
    start_index = last_index - (num_indexes * 5)
    return {
        'field': field,
        'grid_indexes': range(start_index, last_index+1, 5)
    }

class CycleListNode(Node):
    def __init__(self, list_variable, template_variable):
        self.list_variable = list_variable
        self.template_variable = template_variable

    def render(self, context):
        if self not in context.render_context:
            # First time the node is rendered in template
            context.render_context[self] = itertools_cycle(context[self.list_variable])
        cycle_iter = context.render_context[self]
        value = cycle_iter.next()
        if self.template_variable:
            context[self.template_variable] = value
        return ''

@register.tag
def cycle_list(parser, token):
    args = token.split_contents()
    if len(args) != 4 or args[-2] != 'as':
        raise TemplateSyntaxError(u"Cycle_list tag should be in the format {% cycle_list list as variable %}")
    return CycleListNode(args[1], args[3])

@register.filter
def get_photo_label(counter):
    return photo_order[counter]

@register.filter
def to_readable(value):
    value = value.replace('-', ' ')
    value = value.replace('_', ' ')
    return value.title()

@register.filter
def filetype(value):
    return value.split('.')[-1]
