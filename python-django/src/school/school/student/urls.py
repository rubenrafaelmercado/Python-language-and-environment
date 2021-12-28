from django.urls import path
from . import views


urlpatterns = [
    path('time', views.current_datetime),
    path('', views.get_students),    
    path('add/', views.add_student),
    path('<int:id_student>/', views.get_student),
]






