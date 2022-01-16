from django.db.models import fields
from django.utils.translation import gettext_lazy as _

from . import validators


class ISBNField(fields.CharField):
    """
    https://www.isbn-international.org/
    """

    default_validators = [validators.ISBNValidator()]
    description = _("The International Standard Book Number")

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs.setdefault('max_length', 13)
        super().__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 13:
            del kwargs['max_length']
        return name, path, args, kwargs


class DOIField(fields.CharField):
    """
    http://www.doi.org/index.html
    """

    default_validators = [validators.DOIValidator()]
    description = _("A Digital Object Identifier")

    def __init__(self, verbose_name=None, name=None, **kwargs):
        # it is hard to tell the max length of DOI,
        # but it should be less than 255
        kwargs.setdefault('max_length', 255)
        super().__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 255:
            del kwargs['max_length']
        return name, path, args, kwargs


class ISSNField(fields.CharField):
    """
    https://portal.issn.org/
    """

    default_validators = [validators.ISSNValidator()]
    description = _("The International Standard Serial Number")

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs.setdefault('max_length', 9)
        super().__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 9:
            del kwargs['max_length']
        return name, path, args, kwargs
