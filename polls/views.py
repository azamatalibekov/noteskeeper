from django.shortcuts import render
from django.http import *
from .models import Person

global no
no = 0
global yes
yes = 0

def my(request):
    global no
    global yes

    key = request.POST.get("key")
    if key:
        p = Person(first_name=key)
        p.save()

    data = Person.objects.all()

    Person.objects.filter(first_name=request.GET.get("n")).delete()

    keyno = request.GET.get("no")
    keyyes = request.GET.get("yes")
    if(keyno == "delete"):
        no += 1
    if(keyyes == "done"):yes += 1
    key = request.POST.get("key")

    return render(request,"index.html",context={"data":data,"no":no,"yes":yes,})




