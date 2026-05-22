from django.db import models


class SchoolInfo(models.Model):
    """Singleton model for school general info."""
    name = models.CharField(max_length=300)
    tagline = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    map_embed_url = models.URLField(blank=True, help_text="Google Maps embed URL")
    hero_image = models.ImageField(upload_to='core/', blank=True, null=True)
    logo = models.ImageField(upload_to='core/', blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    student_count = models.PositiveIntegerField(blank=True, null=True)
    teacher_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Maktab haqida ma'lumot"
        verbose_name_plural = "Maktab haqida ma'lumot"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Singleton: only one record allowed
        self.pk = 1
        super().save(*args, **kwargs)



