from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from employee_management_sys.cells.forms import CellForm
# Create your views here.
from employee_management_sys.cells.models import Cells
from employee_management_sys.employees.models import Employee


class CellCreateView(LoginRequiredMixin, views.CreateView):
    form_class = CellForm
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'cells/cell-create.html'
    model = Cells
    # fields = '__all__'
    success_url = reverse_lazy('cell list')


class CellDeleteView(LoginRequiredMixin, views.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'cells/cell-delete.html'
    model = Cells
    fields = '__all__'
    success_url = reverse_lazy('cell list')


class CellDisplayView(LoginRequiredMixin, views.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Cells
    template_name = 'cells/cell-list.html'


class CellManageView(LoginRequiredMixin, views.DetailView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Cells
    template_name = 'cells/cells-manage.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.filter(cell=self.kwargs.get('pk'))
        return context


class CellEditView(LoginRequiredMixin, views.UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Cells
    template_name = 'cells/cells-edit.html'
    success_url = reverse_lazy('cell list')
    fields = '__all__'

