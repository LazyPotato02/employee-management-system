from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from employee_management_sys.materials.forms import MaterialForm
from employee_management_sys.materials.models import Materials


# Create your views here.

class MaterialAddView(view.CreateView):
    model = Materials
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('material list')
    success_url = reverse_lazy('material list')
    template_name = 'materials/material-create.html'
    form_class = MaterialForm


class MaterialListView(view.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('material list')
    model = Materials
    template_name = 'materials/material-list.html'

class MaterialEditView(view.UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('material list')
    model = Materials
    template_name = 'materials/material-edit.html'
    success_url = reverse_lazy('material list')
    form_class = MaterialForm


class MaterialDeleteView(view.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('material list')
    template_name = 'materials/material-delete.html'
    model = Materials
    fields = '__all__'
    success_url = reverse_lazy('material list')