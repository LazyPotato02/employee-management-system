from django.urls import path

from employee_management_sys.orders.views import OrderAddView, OrderListView, OrderEditView, OrderDeleteView

urlpatterns = [
    path('add', OrderAddView.as_view(), name='order add'),
    path('list', OrderListView.as_view(), name='order list'),
    path('edit/<int:pk>', OrderEditView.as_view(), name='order edit'),
    path('delete/<int:pk>',OrderDeleteView.as_view(), name='order delete')
]
