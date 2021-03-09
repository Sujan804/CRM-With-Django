from django import forms
from django.db.models import fields
from django.forms.fields import CharField
from .models import Lead, User

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = {
            'first_name',
            'last_name',
            'age',
            'agent'
        }

# class UserLeadForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields ={
#             '__all__'
#         }


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
    # agent = forms.EmailField()
