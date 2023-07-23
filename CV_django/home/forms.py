from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Your nameee ae!!!")
    age = forms.IntegerField()
    flag = forms.BooleanField()
