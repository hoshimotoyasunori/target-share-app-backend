from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('target', views.TargetViewSet)
router.register('comment', views.CommentViewSet)


urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('mytarget/', views.MyTargetListView.as_view(), name='mytarget'),
    path('', include(router.urls))
]
