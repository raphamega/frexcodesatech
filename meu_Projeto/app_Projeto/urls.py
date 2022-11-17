from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
   # path('', views.index, name='home-page'),
    path('', views.lista, name='lista-views'),
    path('lista/<int:id>', views.usuario, name='user-views'),
    path('novo/', views.novoUsuario, name='new-views'),
    path('edit/<int:id>', views.editUsuario, name='edit-views'),
    path('delete/<int:id>', views.delUsuario, name='edit-views'),

]