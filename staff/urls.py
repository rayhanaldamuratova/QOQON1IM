from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('leaders/', views.leaders, name='leaders'),
    path('teachers/', views.teachers, name='teachers'),
    path('<int:pk>/', views.staff_detail, name='detail'),
]



