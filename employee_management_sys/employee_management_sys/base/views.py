from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from employee_management_sys.base.forms import UserUpdateForm, UserCreateForm

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


class UserCreateView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = reverse_lazy('index')
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)
    # TODO:
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            user_group = Group.objects.get(name='Viewer')

            user.groups.add(user_group)

            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True
    name = 'login'


def custom_page_not_found_view(request, exception):
    return render(request, '404.html')

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, '403.html', {})

def custom_bad_request_view(request, exception=None):
    return render(request, "400.html", {})