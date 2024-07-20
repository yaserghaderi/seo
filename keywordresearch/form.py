# forms.py
from django import forms
from .models import KeywordsRank

class SimpleKeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordsRank
        fields = ['keyword']
