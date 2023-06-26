from django.forms import ModelForm
from carsharing.models import Auto


class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ('vin_code', 'auto_model')

        widgets = {
            'vin_code': TextInput(attrs={
                'class': 'input vin_code_input',
                'placeholder': 'Vin'
            }),
            'auto_model': Select(attrs={
                'class': 'input auto_model_input select',
                'placeholder': 'MODEL'
            })
        }
