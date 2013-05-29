from django.db import models
from django_extensions.db.fields import UUIDField

from helpers import make_uuid

class UUIDModel(models.Model):
    uuid = UUIDField(unique=True, default=make_uuid, editable=False)

    class Meta:
        abstract = True
