from rest_framework import serializers
from .models import Profile,Post
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('email', 'name', 'bio','profile_image','location')
        

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','title','description','url','image')
        
        
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts = PostSerializer(many=True,read_only=True)   
    
    
    class Meta:
        model = User
        fields = ('id','url','username','profile','posts')   