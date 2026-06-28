from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    national_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    def __str__(self):
        return self.user.username