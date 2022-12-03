from django.urls import path

from employee_management_sys.cells.views import CellCreateView, CellDeleteView, CellDisplayView

urlpatterns = [
    path('create', CellCreateView.as_view(), name='cell creation'),
    path('delete/<int:pk>', CellDeleteView.as_view(), name='cell deletion'),
    path('list', CellDisplayView.as_view(), name='cell list'),

]