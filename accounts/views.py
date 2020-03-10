from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import customempregistrationform,userregistrationform

def employeeregistrationpage(request):
    if request.method=="POST":
        uform=customempregistrationform(request.POST)
        if uform.is_valid():
            uform.save()
            messages.success,(request,("Account created as employee"))
            return redirect("/")
    else:
        uform = customempregistrationform
    return render(request,'accounts/userregistration.html',context={'uform':uform })
# def userloginpage(request):
#     context={}
#     return render(request,'accounts/userloginpage.html',context)

def userregistrationpage(request):
    if request.method=="POST":
        uform=userregistrationform(request.POST)
        if uform.is_valid():
            uform.save()
            messages.success,(request,("Account created as User"))
            return redirect("/")
    else:
        uform = userregistrationform
    return render(request,'accounts/userregistration.html',context={'uform':uform })


