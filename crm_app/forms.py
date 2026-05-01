from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["name", "service", "document", "date_created", "expiry_date", "amount"]
        widgets = {
            "date_created": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", "class": "form-control"}),
            "expiry_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", "class": "form-control"}),

        }
        