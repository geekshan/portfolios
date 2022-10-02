from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('profile2/', views.ProfileSecond.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('personAPI/', views.PersonView.as_view()),
    path('WeatherAPI/', views.WeatherView.as_view()),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]
