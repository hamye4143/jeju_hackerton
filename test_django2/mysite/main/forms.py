from django import forms 
from .models import Mentor

class TopicForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['이과', '문과', '예체능']
