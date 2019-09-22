from django.urls import path

from . import apis

urlpatterns = [
  path('login/', apis.login, name='login'),
  path('greet/', apis.greet, name='greet'),
  path('logout/', apis.logout, name='logout'),
  path('article/',apis.article, name='article'),
  path('article/<name>',apis.article, name='article'),
  path('article/<tag>/<name>',apis.article, name='article'),
]