from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('olympiad', _('Olimpiada')),
        ('sport', _('Sport')),
        ('science', _('Fan')),
        ('art', _("San'at")),
        ('other', _('Boshqa')),
    ]

    LEVEL_CHOICES = [
        ('school', _('Maktab')),
        ('district', _('Tuman')),
        ('regional', _('Viloyat')),
        ('national', _('Respublika')),
        ('international', _('Xalqaro')),
    ]

    student_name = models.CharField(max_length=200)
    title = models.CharField(max_length=300, help_text="Yutuq nomi")
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='olympiad')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='district')
    place = models.PositiveSmallIntegerField(blank=True, null=True, help_text="O'rin (1, 2, 3)")
    date = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to='achievements/', blank=True, null=True)
    teacher_name = models.CharField(max_length=200, blank=True, help_text="Rahbar o'qituvchi")
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Yutuq")
        verbose_name_plural = _("Yutuqlar")
        ordering = ['-date']

    def __str__(self):
        return f"{self.student_name} — {self.title}"



