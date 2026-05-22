from django.db import models


class StaffMember(models.Model):
    ROLE_CHOICES = [
        ('leader', 'Rahbar'),
        ('teacher', "O'qituvchi"),
    ]

    SUBJECT_CHOICES = [
        ('math', 'Matematika'),
        ('physics', 'Fizika'),
        ('chemistry', 'Kimyo'),
        ('biology', 'Biologiya'),
        ('history', 'Tarix'),
        ('uzbek', "O'zbek tili va adabiyoti"),
        ('english', 'Ingliz tili'),
        ('russian', 'Rus tili'),
        ('it', 'Informatika'),
        ('geography', 'Geografiya'),
        ('sport', 'Jismoniy tarbiya'),
        ('art', 'Tasviriy san\'at'),
        ('other', 'Boshqa'),
    ]

    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    position = models.CharField(max_length=200, help_text="Lavozim, masalan: Maktab direktori")
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, blank=True, null=True,
                                help_text="Faqat o'qituvchilar uchun")
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=300, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0, help_text="Tartib raqami (kichik = yuqori)")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} — {self.position}"



