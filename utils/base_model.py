from typing import Self, Optional
from uuid import uuid4, UUID

from django.db.models import Model, DateTimeField, UUIDField
from django.contrib import admin
from django.core.exceptions import ValidationError as DjangoValidationError

from bookshop.errors import RecordNotFound, ValidationError


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
    def find(cls, id: int) -> Self:
        """Find a model by id. Raises bookshop.errors.RecordNotFound if the model is not found."""
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            raise RecordNotFound(cls, {"id": id})


class UUIDMixin(Model):
    class Meta:
        abstract = True

    uuid = UUIDField(default=uuid4, null=False, unique=True)

    @classmethod
    def find_by_uuid(cls, uuid: UUID) -> Optional[Self]:
        """Find a model by uuid. Raises bookshop.errors.RecordNotFound if the model is not found."""
        try:
            return cls.objects.get(uuid=uuid)
        except cls.DoesNotExist:
            raise RecordNotFound(cls, {"uuid": uuid})
        except DjangoValidationError as e:
            raise ValidationError(e)
