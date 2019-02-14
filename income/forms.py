from django import forms
from income.models import Adult

def tuple2dict(tuple_object):
    return [{x:y} for x, y in tuple_object]

class AdultForm(forms.Form):
    model = Adult
    age = forms.ChoiceField(choices=Adult.AGE_CHOICES, required=True)
    education = forms.ChoiceField(choices=Adult.EDU_CHOICES, required=True)
    years_education = forms.ChoiceField(choices=Adult.NUM_CHOICES, required=True)
    marital_status = forms.ChoiceField(choices=Adult.STA_CHOICES, required=True)
    occupation = forms.ChoiceField(choices=Adult.OCC_CHOICES, required=True)
    relationship = forms.ChoiceField(choices=Adult.REL_CHOICES, required=True)
    race = forms.ChoiceField(choices=Adult.RAC_CHOICES, required=True)
    gender = forms.ChoiceField(choices=Adult.SEX_CHOICES, required=True)
    hours_per_week = forms.ChoiceField(choices=Adult.HRS_CHOICES, required=True)
