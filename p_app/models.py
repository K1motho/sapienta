from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Saying (models.Model):
    CULTURES = [
        ('Greek', 'Ancient Greek'),
        ('Hebrew', 'Hebrew'),
        ('Latin', 'Latin'),
        ('West African', 'West African'),
    ]

    TONES = [
       ('joyful', 'Joyful'),
        ('cautionary', 'Cautionary'),
        ('solemn', 'Solemn'),
        ('reflective', 'Reflective'),
        ('humorous', 'Humorous'), 
    ]

    original_text = models.TextField()
    translation = models.TextField()
    explanation = models.TextField()
    culture = models.CharField(max_length=30, choices=CULTURES)
    tone = models.CharField(max_length=30, choices=TONES)
    source = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.translation[:50]}..."
    
class SavedSAyings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saying = models.ForeignKey(Saying, on_delete=models.CASCADE)
    Saved_at = models.DateField(auto_now_add=True)