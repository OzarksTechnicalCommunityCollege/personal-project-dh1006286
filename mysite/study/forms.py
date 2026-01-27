from django import forms
from .models import Card

class MakeCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'false_answer_1', 'false_answer_2', 'false_answer_3']