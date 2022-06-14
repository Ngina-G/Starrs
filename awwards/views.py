from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,PostForm,UpdateUserForm,UpdateUserProfileForm,RatingForm
from rest_framework import viewsets
from .models import Profile,Post,Rating
from .serializers import ProfileSerializer,UserSerializer,PostSerializer
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import random
from random import randrange

# Create your views here.
def  index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False )
            post.user = request.user
            post.save()
    else:
        form = PostForm()      
    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]
        print(random_post)
    except Post.DoesNotExist:
        posts=None

    return render(request, 'index.html', {'posts': posts,'form': form,'random_post': random_post})


def  signup(request):
    if request.method == 'POST':    
        form = SignupForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else: 
        form = SignupForm
    return render(request, 'registration/signup.html', {'form': form}) 


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')   
def  user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile',username=request.user.username)
    context = {
        'user_prof:user_prof,'
    }
    return render(request, 'awwards/user_profile.html', context)


@login_required(login_url='login') 
def  edit_userprofile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST': 
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request. FILES,instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid:
            user_form.save()
            prof_form.save(commit=False)
            return redirect('profile',user.username)
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'prof_form': prof_form,
    }         
        
    return render(request, 'awwards/edit_userprofile.html',context)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 