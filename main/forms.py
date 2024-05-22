from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Логин', required=True)
    fullname = forms.CharField(max_length=255, label='ФИО', required=True)
    email = forms.EmailField(max_length=255, label='Почта', required=True)
    phone_number = forms.CharField(max_length=255, label='Номер телефона', required=True)
    password = forms.CharField(max_length=255, label='Пароль', widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError(_('Пароль должен содержать больше 6 символов.'), code='password_too_short')
        if not any(char.isupper() for char in password):
            raise ValidationError(_('Пароль должен содержать вверхний регистр.'), code='password_no_uppercase')
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user



    class Meta: 
        model = User
        fields = 'username', 'fullname', 'email', 'phone_number', 'password'
        