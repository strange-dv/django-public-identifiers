from django.core import validators


class ISBNValidator(validators.RegexValidator):
    pass


class DOIValidator(validators.RegexValidator):
    pass


class ISSNValidator(validators.RegexValidator):
    pass
