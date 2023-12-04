
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views

from todos.views import index, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('sobre/', sobre, name = 'sobre')
]
