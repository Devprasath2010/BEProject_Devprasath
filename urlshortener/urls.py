from django.urls import path
from .views import Home, redirect

urlpatterns = [
	path('', Home, name="Home" ),
	path('<str:url>/', redirect, name="redirect")
]
