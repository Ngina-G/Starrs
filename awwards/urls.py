from django.urls import include,path
from . import views
from rest_framework import  routers

router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('posts',views.PostViewSet)
router.register('profile',views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/',include('django.contrib.auth.urls'), name='account'),
    path('api/', include(router.urls)),
    path('profile/<username>', views.profile, name='profile'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('<username>/profile',views.user_profile, name='user profile'),    
    path('profile/<username>/setting', views.edit_userprofile, name='edit'), 
    path('project/<post>',views.projectPost,name='project'),    
    path('search/',views.search_project,name='search'), 
]
