from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from django_extensions.db.models import TimeStampedModel
from django_languages.fields import LanguageField


class News(TimeStampedModel):
    headline = models.CharField(verbose_name=_('Headline'), max_length=255)
    content = models.TextField(verbose_name=_('Content'))
    publication_date = models.DateField(verbose_name=_('Publication Date'))
    language = LanguageField()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
