
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views, include

from todos.views import index, sobre
from userProfile.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('sobre/', sobre, name = 'sobre'),
    path('signup/', signup, name = 'signup'),
    path('login/', views.LoginView.as_view(template_name = 'userProfile/login.html'), name = 'login'),
    path('logout/', views.LoginView.as_view(), name = 'logout'),
    path('dashboard/', include('dashboard.urls')),
]
