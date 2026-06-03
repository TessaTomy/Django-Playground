from django.urls import path
from . import views

urlpatterns = [
   path('', views.sam_home, name='sam_home'),
]