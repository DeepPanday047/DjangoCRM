from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters, start with a capital letter, and include at least one number or special character.'
        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = 'Enter the same password as above, for verification.'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),label='')
    last_name =forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),label='')
    email = forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Email','class':'form-control'}),label='')
    phone = forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Phone','class':'form-control'}),label='')
    address =forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Address','class':'form-control'}),label='')
    city = forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'City','class':'form-control'}),label='')
    state = forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'State','class':'form-control'}),label='')
    zipcode=forms.CharField(max_length= 50,required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Zipcode','class':'form-control'}),label='')


    class Meta:
        model = Record
        exclude = ('user',)
