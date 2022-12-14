from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee_management_sys.base.urls')),
    path('cells/',include('employee_management_sys.cells.urls')),
    path('employees/',include('employee_management_sys.employees.urls')),
    path('orders/',include('employee_management_sys.orders.urls')),
    path('material/',include('employee_management_sys.materials.urls')),
]
handler404 = 'employee_management_sys.base.views.custom_page_not_found_view'
handler500 = 'employee_management_sys.base.views.custom_error_view'
handler403 = 'employee_management_sys.base.views.custom_permission_denied_view'
handler400 = 'employee_management_sys.base.views.custom_bad_request_view'