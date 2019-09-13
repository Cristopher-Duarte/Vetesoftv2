from django.contrib import admin
from django.urls import path,include
from VeteSoft.links import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('VeteSoft.links'))
]