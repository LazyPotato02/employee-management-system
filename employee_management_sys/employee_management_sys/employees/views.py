from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
from employee_management_sys.employees.models import Employee


class EmployeeCreateView(LoginRequiredMixin,views.CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('index')
    template_name = 'employee-create.html'
    model = Employee
    fields = '__all__'
