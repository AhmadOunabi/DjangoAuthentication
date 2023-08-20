from django.contrib import admin
from django.urls import path, include
from .views import home ,signup, activate, signin, profile

urlpatterns = [
    path('loggg/', signin),
    path('',home),
    path('signup/', signup),
    path('signup/<slug:username>/activate', activate),
    path('profile/', profile)
    
]
