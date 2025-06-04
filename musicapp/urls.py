from django.urls import path
from musicapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.movies_list, name='home'),
    path('mudic/<int:id>/', views.movies_list, name='music'),
    path('song/<int:id>/', views.video_list, name='song'),
    path('nav/', views.navibar, name='nav'),
    path('search/', views.search, name='search'),
    path('playlist/', views.create_playlist, name='playlist'),

]