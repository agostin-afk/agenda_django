from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Primeiro nome',
            }
        ),
        help_text= 'insira o primeiro nome do contato'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['first_name'].widget.atttr.update({
        #})
    
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',  
                )
    def clean(self):
        #cleaned_data = self.cleaned_data
        self.add_error(
            None,
            ValidationError(
                'mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()
