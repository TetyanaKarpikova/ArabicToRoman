from django import forms


class IntForm(forms.Form):
    input_date = forms.CharField(label="Арабские/римские цифры")

