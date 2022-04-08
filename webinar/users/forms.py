from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """Form used in the admin to create new users."""

    class Meta(auth_forms.UserCreationForm.Meta):
        model = User


class UserChangeForm(auth_forms.UserChangeForm):
    """Form used in the admin to change the data related to an existing user."""

    class Meta(auth_forms.UserChangeForm.Meta):
        model = User
