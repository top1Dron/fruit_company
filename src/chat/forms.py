from django import forms
from django.contrib.auth import forms as auth_forms, models

from .models import ChatMessage


class CustomUserCreationForm(auth_forms.UserCreationForm):

    class Meta(auth_forms.UserCreationForm):
        model = models.User
        fields = ('username', 'email', 'first_name', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'id_signup_username'
        self.fields['username'].label = 'Никнейм пользователя'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = 'Email'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Подтвердите пароль'

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        if models.User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует!")
        return self.cleaned_data


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text']


class LoginForm(forms.Form):
    username = forms.CharField(label='Никнейм', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))