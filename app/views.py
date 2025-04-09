from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_school(request):
    ESFO=SchoolForm()
    d={"ESFO":ESFO}
    if request.method=="POST":
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['scname']
            sl=SFDO.cleaned_data['sclocation']
            sp=SFDO.cleaned_data['scprincipal']
            School.objects.get_or_create(scname=sn,sclocation=sl,scprincipal=sp)
            return HttpResponse('school is created')
    return render(request,'insert_school.html',d)