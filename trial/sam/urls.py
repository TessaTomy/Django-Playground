from django.urls import path
from . import views

urlpatterns = [
   path('', views.sam, name='sam'),
   path('add_state/', views.add_state, name='add_state'),
   path('state_list/', views.state_list, name='state_list'),
]