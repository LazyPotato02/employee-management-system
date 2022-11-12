from django.urls import path

from employee_management_sys.employees.views import EmployeeCreateView

urlpatterns = [
    path('create/', EmployeeCreateView.as_view(),name='employee creation')
]