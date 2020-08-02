from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm): 

    class Meta:
        model = Jasoseol
        # jasoseol에 대응되는 필드를 만들어줌
        fields = ("title", 'content',)