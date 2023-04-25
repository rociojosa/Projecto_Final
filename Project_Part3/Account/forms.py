from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from Account.models import Avatar
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label = 'Contreseña', widget=forms.PasswordInput)
    password2= forms.CharField(label = ' Repetir contreseña', widget=forms.PasswordInput)
    is_staff = forms.BooleanField()
    imagen = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "password1", "password2"]
        help_texts = {k: "" for k in fields}
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar e-mail")
    password1= forms.CharField(label = 'Contreseña', widget=forms.PasswordInput)
    password2= forms.CharField(label = ' Repetir contreseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = {"user", "imagen"}
        