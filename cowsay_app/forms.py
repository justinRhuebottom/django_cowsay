from django import forms
from cowsay_app.models import input_text

class InputTextForm(forms.ModelForm):
    class Meta:
        model = input_text
        fields = '__all__'