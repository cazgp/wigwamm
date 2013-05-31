from django import forms
from django.db.models import CharField

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]


class OneCharChoiceField(CharField):
    def __init__(self, *args, **kwargs):
        super(OneCharChoiceField, self).__init__(*args, **kwargs)
        self.max_length = 1
