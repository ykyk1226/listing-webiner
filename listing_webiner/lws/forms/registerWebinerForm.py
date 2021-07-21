from django import forms


class RegisterWebinerForm(forms.Form):
    webiner_list = forms.CharField(max_length=1024)
