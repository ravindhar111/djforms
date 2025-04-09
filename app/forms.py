from django import forms


class SchoolForm(forms.Form):
    scname=forms.CharField()
    sclocation=forms.CharField()
    scprincipal=forms.CharField()