from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from employee_management_sys.materials.models import Materials


# Create your views here.

class MaterialAddView(view.CreateView):
    model = Materials
    fields = '__all__'
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('material list')
    success_url = reverse_lazy('material list')
    template_name = 'materials/material-create.html'

class MaterialListView(view.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Materials
    template_name = 'materials/material-list.html'

class MaterialEditView(view.UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    model = Materials
    template_name = 'materials/material-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('material list')

class MaterialDeleteView(view.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'materials/material-delete.html'
    model = Materials
    fields = '__all__'
    success_url = reverse_lazy('index')