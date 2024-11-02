from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profile_avatars/', blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

    def __str__(self):
        return self.user.username
