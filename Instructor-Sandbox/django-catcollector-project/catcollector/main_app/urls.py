from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name='home'),
    path('cats/', views.cats_index, name='index')
]

