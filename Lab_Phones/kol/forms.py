from django import forms
from kol.models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'