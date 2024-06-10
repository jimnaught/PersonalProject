from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('ourwork/', views.ourwork, name='ourwork'),
    path('about/', views.about, name='about')
]