from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=  forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholer':'Email Address'}))
    first_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholer':'First Name'}))
    last_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholer':'Last Name'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = 'Choose a unique username.'

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters, start with a capital letter, and include at least one number or special character.'

        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = 'Enter the same password as above, for verification.'