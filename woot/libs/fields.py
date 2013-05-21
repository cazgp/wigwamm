from django.db.models import CharField

class OneCharChoiceField(CharField):
    def __init__(self, *args, **kwargs):
        super(OneCharChoiceField, self).__init__(*args, **kwargs)
        self.max_length = 1
