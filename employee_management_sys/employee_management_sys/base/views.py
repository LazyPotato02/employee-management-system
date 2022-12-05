from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from employee_management_sys.base.forms import  UserUpdateForm

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'base.html'


class UserEditView(LoginRequiredMixin, views.UpdateView):
    form_class = UserUpdateForm
    model = UserModel
    template_name = 'users/edit.html'
    # fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('index')

class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'users/delete.html'
    success_url = reverse_lazy('index')

