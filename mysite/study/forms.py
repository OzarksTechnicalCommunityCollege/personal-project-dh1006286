from django import forms
from .models import Card, Set
from django.contrib.auth import get_user_model

class MakeCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'false_answer_1', 
                  'false_answer_2', 'false_answer_3']

class MakeSetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['name', 'tags']

# User forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label = 'password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label = 'Repeat password',
        widget = forms.PasswordInput,
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']
