from django.urls import include,path
from . import views
from rest_framework import  routers

router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('posts',views.PostViewSet)
router.register('profile',views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('account/',include('django.contrib.auth.urls'), name='account'),
    path('api/', include(router.urls)),
]
