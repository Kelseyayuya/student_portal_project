from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # dashboard root
    path('about/', views.about, name='about'),
]
