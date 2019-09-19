from django.urls import path

from . import apis

urlpatterns = [
  path('login/', apis.login, name='login'),
  path('greet/', apis.greet, name='greet'),
  path('logout/', apis.logout, name='logout'),
]