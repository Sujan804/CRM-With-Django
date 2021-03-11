from django import forms
from django.db import models
from django.forms import fields
from leads.models import Agent

class AgentModelForm(forms.ModelForm):
   class Meta:
       model = Agent
       fields ={
           'user',
       }
