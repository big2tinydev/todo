from todo.models import Image
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'name',
            'image',
        ]
