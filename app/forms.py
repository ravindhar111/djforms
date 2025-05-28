from django import forms
from app.models import *


def valid_for_len(a):
    if len(a)<5:
        raise forms.ValidationError('Invalid data')
    

class SchoolForm(forms.Form):
    scname=forms.CharField(validators=[valid_for_len])
    sclocation=forms.CharField()
    scprincipal=forms.CharField()

class SchoolModelForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'
        

class StudentForm(forms.Form):
    scname=forms.CharField()
    stname=forms.CharField()
    stage=forms.IntegerField()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

