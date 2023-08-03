from django import forms
from bankingapp.models import FormData

class FormPageForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = '__all__'