from django.core import validators
from django.utils.translation import gettext_lazy as _


class ISBNValidator(validators.RegexValidator):
    # example: 978-1-56619-909-4

    regex = r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$"
    message = _('Enter a valid ISBN.')


class DOIValidator(validators.RegexValidator):
    # example: 10.1111/j.1365-2575.2012.00413.x

    regex = r"^.*(10\.[A-Za-z0-9.\/-]+)(?<!\.)(?=[ ]|\.).*$"
    message = _('Enter a valid DOI.')


class ISSNValidator(validators.RegexValidator):
    # example: 0208-6336

    regex = r"^[\S]{4}\-[\S]{4}$"
    message = _('Enter a valid ISSN.')
