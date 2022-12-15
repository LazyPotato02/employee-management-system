from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.core import validators

from employee_management_sys.base.validators import validate_only_letters

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {
            'username': auth_forms.UsernameField,
        }


class UserCreateForm(auth_forms.UserCreationForm):
    username = forms.CharField(
        label='Username', validators=(
            validators.MinLengthValidator(3),
        ),
    )
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': auth_forms.UsernameField,
        }
        help_texts = {
            'username': None,
        }


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = UserModel

        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserModel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Email Already Exists")
        return email
