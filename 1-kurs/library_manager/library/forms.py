from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Ism",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Familya",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familyangiz'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Foydalanuvchi nomi",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'id_username',
            'autocomplete': 'off'
        })
    )
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kiriting'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default password validators (make it simpler)
        self.fields['password1'].help_text = 'Kamida 4 ta belgi kiriting.'
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 4:
            raise ValidationError('Parol kamida 4 ta belgidan iborat bo\'lishi kerak.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Parollar bir xil emas.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
