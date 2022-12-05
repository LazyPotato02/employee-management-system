from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from employee_management_sys.base.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class EmployeeModelAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
