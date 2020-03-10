from .models import Bugs
from django import forms


class RaisebugForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('name','priority','issue','discription','status','attachments')
