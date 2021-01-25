from django import forms
from .models import listItem

class dateInput(forms.DateInput):
    input_type='date'

class addItem(forms.ModelForm):
    class Meta:
        model = listItem
        fields = ('name', 'quantity', 'unit', 'status', 'date')
        widgets = {'date': dateInput}

    














        '''UNITS = [
            ('kg', 'Kgs'),
            ('gm', 'Grams'),
            ('l', 'Litres'),
            ('ml', 'Mililitres'),
            ('m', 'Metres'),
            ('cm', 'Centimetres')
        ]
        STAT = (
            ('B','Bought'),
            ('L','Left'),
            ('N','Not-Available')
        )
        name = forms.CharField(label="Enter item name")
        quantity = forms.IntegerField(label="Amount")
        unit = forms.ChoiceField(label="Unit", choices=UNITS)
        status = forms.ChoiceField(label="Status", choices=STAT)'''



    
