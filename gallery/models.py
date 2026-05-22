from django.db import models
from django.utils import timezone


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery/covers/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albomlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def photo_count(self):
        return self.photos.count()


class GalleryPhoto(models.Model):
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/photos/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"
        ordering = ['order']

    def __str__(self):
        return f"{self.album.title} — {self.pk}"



