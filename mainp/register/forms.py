from django import forms
from django.contrib.auth.models import User

class Registerform(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    conpassword = forms.CharField(max_length=20, widget = forms.PasswordInput())

    def Inputregister(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            conpassword = self.cleaned_data['conpassword']
            if password == conpassword and password:
                return conpassword
            raise forms.ValidationError('Pass not match!!!')

    
    def Inputuser(self):
        username = self.cleaned_data['username']
        if username == username:
            return username
        raise forms.ValidationError('The name Account has existing!!!')

    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],
        email = self.cleaned_data['email'],password = self.cleaned_data['password'] )