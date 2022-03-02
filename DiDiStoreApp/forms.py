from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"required class":"registration_inputs"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"required class":"registration_inputs"}))


class RegistrationForm(UserCreationForm):
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"required class":"registration_inputs","id":"name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"required class":"registration_inputs","id":"email"}))
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"required class":"registration_inputs","id":"surname"}))
    password1 = forms.CharField(label="Пароль 1", widget=forms.PasswordInput(attrs={"required class":"registration_inputs","id":"pass"}))
    password2 = forms.CharField(label="Пароль 2", widget=forms.PasswordInput(attrs={"required class":"registration_inputs","id":"conf_pass"}))

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

