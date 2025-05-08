from typing import Self, Optional
from uuid import uuid4

from django.db.models import Model, DateTimeField, UUIDField
from django.contrib import admin


def register_admin(model_cls):
    admin.site.register(model_cls)
    return model_cls


class BaseModel(Model):
    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        d = vars(self)
        d.pop("_state", None)
        return str(d)

    @classmethod
    def find(cls, id: int) -> Optional[Self]:
        """Find a model by id. Returns None if the model is not found."""
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None


class UUIDMixin:
    uuid = UUIDField(default=uuid4, null=False, unique=True)
