from django import forms
from .models import Details

class DetailsForm(forms.ModelForm):
 class Meta:
  model = Details
  fields = '__all__'
  labels = {'image':'Image'}
