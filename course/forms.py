from django import forms
from .models import Signup

# class StudentForm(forms.Form):
#     name = forms.CharField(label = "Full Name", max_length=100)

# class RegistrationForm(forms.Form):
#     firstName = forms.CharField(label="First Name",max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-100'}))
#     NameLast = forms.CharField(label="Last Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control w-100'}))
#     email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control w-100'}))
#     Password = forms.CharField(label="Create Password",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control w-100'}))
#     Password1 = forms.CharField(label="confirm Password",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control w-100'}))

class StudentForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"