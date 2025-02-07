from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check),
    path('employees', views.get_employees),
    path('employees/get/<int:id>', views.get_employee),
    path('employees/add', views.add_employee),
    path('employees/edit/<int:id>', views.update_employee),
    path('employees/delete/<int:id>', views.delete_employee),
]