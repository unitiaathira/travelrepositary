from . import views
from django.urls import path

urlpatterns = [
    path('', views.home3, name='homepage3'),
    path('about/', views.aboutfun, name='aboutpage'),
    path('contact/', views.contactfun, name='contactpage'),
    path('add/', views.addition, name='additions')
]