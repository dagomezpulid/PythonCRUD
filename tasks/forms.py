from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "placeholder": "John Doe",
                "maxlength": "16",
                "minlength": "6",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "password1",
                "id": "password1",
                "type": "password",
                "placeholder": "password",
                "maxlength": "22",
                "minlength": "8",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "password2",
                "id": "password2",
                "type": "password",
                "placeholder": "password",
                "maxlength": "22",
                "minlength": "8",
            }
        )

    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
