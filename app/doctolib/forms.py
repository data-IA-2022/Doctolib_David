"""forms Module"""
from django import forms
from doctolib.models import GeneralFormRecord, StressFormRecord


class PostGeneralForm(forms.ModelForm):
    """_summary_

    Args:
        forms (class): django class for forms
    """
    class Meta:
        model = GeneralFormRecord
        exclude = [] # pylint: disable=W5104:modelform-uses-exclude


class PostStressForm(forms.ModelForm):
    """class for stress form

    Args:
        forms (class): _description_
    """
    class Meta:
        model = StressFormRecord
        exclude = [] # pylint: disable=W5104:modelform-uses-exclude
