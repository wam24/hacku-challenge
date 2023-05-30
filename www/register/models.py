from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=256, null=False, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=256, null=False, verbose_name=_("Last Name"))
    email = models.CharField(max_length=512, unique=True, verbose_name=_("Email"))
    country = CountryField()

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
