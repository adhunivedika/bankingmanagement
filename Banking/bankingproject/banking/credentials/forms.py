from django import forms
from .models import RegisterFormModel


class RegisterForm(forms.ModelForm):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= RegisterFormModel
        fields=('username','password','confirm_password',)
    def clean(self):
        cleaned_data=super().clean()
        valpwd=self.cleaned_data['password']
        valcpwd = self.cleaned_data['confirm_password']
        if valpwd != valcpwd:
            raise forms.ValidationError('Password not match')
