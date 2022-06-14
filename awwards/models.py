from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length =30)
    bio = models.TextField(max_length=255)
    profile_photo = models.ImageField(upload_to='profile/',default ='image.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    
    def __str__(self):
        return f'{self.user.username} profile'
    
  