from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sample
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,  help_text='Required.')
    last_name = forms.CharField(max_length=30,  help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




class CreateSampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ('Name', 'Date', 'Location', 'Description', 'Owner')


class SampleAddForm(ModelForm):
    class Meta:
        model = Sample
        fields = ('Name', 'Date', 'Location', 'Description', 'Owner')
        widgets = {'Owner': forms.HiddenInput()}