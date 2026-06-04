from django.urls import path
from . import views

urlpatterns = [
   path('', views.sam, name='sam'),
   path('add_state/', views.add_state, name='add_state'),
   path('state_list/', views.state_list, name='state_list'),
   path('states/<int:pk>/edit/', views.update_state, name='update_state'),
   path('states/<int:pk>/delete/', views.state_delete, name='state_delete'),
   path('districts/', views.list_districts, name='district_list'),
   path('add_district/', views.add_district, name='add_district'),
   path('add_student/', views.add_student, name='add_student'),
   path('student_list/', views.student_list, name='student_list'),  
   path('get-districts/<int:state_id>/', views.get_districts, name='get_districts'),
]