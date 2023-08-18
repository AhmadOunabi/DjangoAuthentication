from django.contrib import admin
from django.urls import path, include
from .views import home ,signup, activate

urlpatterns = [
    path('',home),
    path('signup/', signup),
    path('signup/<slug:username>/activate', activate),
]