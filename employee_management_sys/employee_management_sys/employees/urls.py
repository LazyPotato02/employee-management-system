from django.urls import path

from employee_management_sys.employees.views import EmployeeCreateView

urlpatterns = [
    # path('')
    path('create/', EmployeeCreateView.as_view(), name='employee creation')
]

# TODO: Create SignUp for employees to track their month progression
# TODO: Create employee/index for where all the employees are listed and buttons are shown for CRUD and manage them
