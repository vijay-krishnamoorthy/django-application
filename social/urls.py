from django.urls import path
from . import views
urlpatterns = [
path('', views.base, name='Homepage'),
path('about/', views.about, name='about'),
path('posts/', views.posts, name='posts'),
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('create_post/', views.create_post, name='create_post'),
path('validate/', views.validate, name='validate'),
]