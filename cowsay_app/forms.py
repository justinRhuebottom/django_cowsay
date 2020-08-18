from django import forms
from cowsay_app.models import text_input

class InputTextForm(forms.ModelForm):
    class Meta:
        model = text_input
        fields = '__all__'