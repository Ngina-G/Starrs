from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30)
    bio = models.TextField(max_length=255)
    profile_image = models.ImageField(upload_to='profile/',default ='image.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', )
    email = models.EmailField(max_length=255, blank=True) 

    def __str__(self):
        return f'{self.user.username}profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    
class Post(models.Model):    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    url = models.URLField(max_length=255)
    image = models.ImageField(default='default.png', upload_to='post_images')
    user = models.ForeignKey(User,default=None,null=True, on_delete=models.CASCADE,related_name='posts')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()
        
class Rating(models.Model):
    rating = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )
    design = models.IntegerField(choices=rating, default=0,blank=True)
    usability = models.IntegerField(choices=rating, default=0, blank=True) 
    content = models.IntegerField(choices=rating, default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
            self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'


