from django import forms
from.models import Field

class DateInput(forms.DateInput):
    input_type = 'date'

class  FieldForm(forms.ModelForm):
    class Meta:
        model= Field
        fields ='__all__'

        widgets ={
            'S_date':DateInput(),
        }
