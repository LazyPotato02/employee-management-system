from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from employee_management_sys.orders.models import Order


# Create your views here.

class OrderAddView(view.CreateView):
    model = Order
    fields = '__all__'
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('order list')
    success_url = reverse_lazy('order list')
    template_name = 'orders/order-create.html'

class OrderListView(view.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Order
    template_name = 'orders/order-list.html'


class OrderEditView(view.UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Order
    template_name = 'orders/order-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('order list')

class OrderDeleteView(view.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'orders/order-delete.html'
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('index')