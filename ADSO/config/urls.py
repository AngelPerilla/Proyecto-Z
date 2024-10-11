from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
]   