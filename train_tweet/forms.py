from django import forms

class InputForm(forms.Form):
    name = forms.CharField(
        label='電車名',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
