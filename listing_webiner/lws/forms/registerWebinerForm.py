from django import forms


class RegisterWebinerForm(forms.Form):
    webiner_lists = forms.CharField(max_length=1024)
