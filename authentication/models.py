from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from util.code_generator import generate_code

# Create your models here.

class Profile (models.Model):
    user= models.OneToOneField(User,related_name='user_profile', on_delete=models.CASCADE)
    image= models.ImageField(upload_to='authentication')
    code= models.CharField(max_length=10, default=generate_code)
        
    def __str__(self):
        return str(self.user)
    
    # Create new Profile for each new User using Signals.
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    