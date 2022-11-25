from django.urls import path, reverse_lazy

from employee_management_sys.base.views import IndexView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', auth_views.LoginView.as_view(template_name='login.html', success_url=reverse_lazy('index'),), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]
