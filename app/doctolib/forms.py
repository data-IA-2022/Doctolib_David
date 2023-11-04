"""forms Module"""
from django import forms
from doctolib.models import General_form_record, Stress_form_record


class PostGeneralForm(forms.ModelForm):
    """_summary_

    Args:
        forms (class): django class for forms
    """
    class Meta:
        model = General_form_record
        exclude = []


class PostStressForm(forms.ModelForm):
    """class for stress form

    Args:
        forms (class): _description_
    """
    class Meta:
        model = Stress_form_record
        exclude = []
