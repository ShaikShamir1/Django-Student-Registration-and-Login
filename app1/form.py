from django import forms
from app1.models import RForm

class RegForm(forms.ModelForm):
    class Meta:
        model=RForm
        fields=['username','password','Profile_photo','number']