from django.db import models
# Импорт для Internationalization (i18n)
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


def validate_not_whitespace(value):
	if not value or value.strip() == '':
		raise ValidationError(
			_('Please enter a non-whitespace string'),
			code='only_whitespace'
		)

class Regions(models.Model):
	created = models.DateTimeField(auto_now_add=True, verbose_name=_('შეიქმნა'))
	updated = models.DateTimeField(auto_now=True, verbose_name=_('განახლდა'))
	name_ge = models.CharField(
		max_length=50,
		verbose_name=_("რეგიონის დასახელება"),
		unique=True,
		blank=False,
		null=False,
		validators=[validate_not_whitespace]
	)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _('Region')
		verbose_name_plural = _('Regions')
		ordering = ['name_ge']

	def __str__(self):
		return self.name_ge


class Districts(models.Model):
	created = models.DateTimeField(auto_now_add=True, verbose_name=_('შეიქმნა'))
	updated = models.DateTimeField(auto_now=True, verbose_name=_('განახლდა'))
	name_ge = models.CharField(
		max_length=50,
		verbose_name=_("რაიონის/ქალაქის დასახელება"),
		unique=True,
		blank=False,
		null=False,
		validators=[validate_not_whitespace]
	)
	region = models.ForeignKey(
		Regions,
		on_delete=models.CASCADE,
		related_name='districts',
		verbose_name=_('რეგიონი'),
		#default=1
	)
	history = HistoricalRecords()

	class Meta:
		verbose_name = _('District')
		verbose_name_plural = _('Districts')
		ordering = ['name_ge']

	def __str__(self):
		return self.name_ge