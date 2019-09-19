
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('auth/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
