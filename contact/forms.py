from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):
    
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
