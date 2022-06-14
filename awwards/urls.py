from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#..............

urlpatterns=[
    path('', views.index, name='home'),
    path('profile/<user_name>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    path('like/<int:pk>', views.LikePost, name='like_image'),
    path('search/', views.search_profile, name='search'),
    path('signup/', views.signup, name ='signup'),
    path('logout/',views.logout_user, name='logout'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)