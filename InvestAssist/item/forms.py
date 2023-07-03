from django import forms
from .models import Item

INPUT_CLASSES = 'w-30 py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }