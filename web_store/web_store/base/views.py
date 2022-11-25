from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'base.html'
