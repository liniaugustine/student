from django.urls import path
from . import views

urlpatterns = [
    path('firstpg', views.firstpg, name='firstpg'),
    path('alogin', views.alogin, name='alogin'),
    path('login', views.login, name='login'),
    path('cracc', views.cracc, name='cracc'),
    path('cracc2', views.cracc2, name='cracc2'),
    path('admin', views.admin, name='admin'),
    path('active', views.active, name='active'),
    path('inactivate/<int:inactiveid>', views.inactivate, name='inactivate'),
    path('inactive', views.inactive, name='inactive'),
    path('activate/<int:activeid>', views.activate, name='activate'),
    path('homepage', views.homepage, name='homepage'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('signout', views.signout, name='signout'),
    path('asignout', views.asignout, name='asignout'),
    
    
]