from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
from employee_management_sys.cells.models import Cells


class CellCreateView(LoginRequiredMixin, views.CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'cells/cell-create.html'
    model = Cells
    fields = '__all__'
    success_url = reverse_lazy('index')


class CellDeleteView(LoginRequiredMixin, views.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'cells/cell-delete.html'
    model = Cells
    fields = '__all__'
    success_url = reverse_lazy('index')


class CellDisplayView(LoginRequiredMixin, views.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Cells
    template_name = 'cells/cell-list.html'


