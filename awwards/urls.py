from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
from . import views
from rest_framework import  routers

router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('posts',views.PostViewSet)
router.register('profile',views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('api/', include(router.urls)),
    path('profile/<username>', views.profile, name='profile'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('<username>/profile',views.user_profile, name='user profile'),    
    path('profile/<username>/setting', views.edit_userprofile, name='edit'), 
    path('project/<post>',views.projectPost,name='post'),    
    path('search/',views.search_project,name='search'), 
    path('logout/',views.logout_user, name='logout'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)