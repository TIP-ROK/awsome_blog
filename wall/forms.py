from django import forms


class SearchingUserForm(forms.Form):
    user = forms.CharField(max_length=100)
