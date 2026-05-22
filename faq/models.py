from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name=_("Savol"))
    answer = models.TextField(verbose_name=_("Javob"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib"))
    is_active = models.BooleanField(default=True, verbose_name=_("Faol"))

    class Meta:
        verbose_name = _("Savol-Javob")
        verbose_name_plural = _("Savol-Javoblar")
        ordering = ['order']

    def __str__(self):
        return self.question



