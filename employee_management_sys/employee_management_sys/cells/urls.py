from django.urls import path

from employee_management_sys.cells.views import CellCreateView, CellDeleteView, CellDisplayView, CellManageView, \
    CellEditView

urlpatterns = [
    path('create', CellCreateView.as_view(), name='cell creation'),
    path('delete/<int:pk>', CellDeleteView.as_view(), name='cell deletion'),
    path('list', CellDisplayView.as_view(), name='cell list'),
    path('manage/<int:pk>', CellManageView.as_view(), name='cell manage'),
    path('edit/<int:pk>', CellEditView.as_view(), name='cell edit')

]
