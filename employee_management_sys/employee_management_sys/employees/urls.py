from django.urls import path

from employee_management_sys.cells.models import Cells
from employee_management_sys.employees.models import Employee
from employee_management_sys.employees.views import EmployeeCreateView, EmployeeListView, EmployeeEditView, \
    EmployeeDeleteView

urlpatterns = [
    path('create/', EmployeeCreateView.as_view(), name='employee creation'),
    path('list/', EmployeeListView.as_view(), name='employee list'),
    path('edit/<int:pk>', EmployeeEditView.as_view(), name='employee edit'),
    path('delete/<int:pk>', EmployeeDeleteView.as_view(), name='employee delete'),
]

# TODO: Create SignUp for employees to track their month progression
# em = Employee(2,'Stoyan', 'Kanev', 'C04', 3 - 1022)
# em.save()
# ce = Cells(3,'C04')
# ce.save()
# ce.employee.add(em)