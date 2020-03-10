from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from .models import Bugs
from .forms import RaisebugForm

# Create your views here.
def home(requset):
    return render(requset,'bugtrack/home.html',context={})

def all_bugs(request):
    bugs=Bugs.objects.all()
    return render (request,'bugtrack/all_bugs.html',context={'bugs':bugs })

@login_required
def raise_bugs(request):
    if request.method=='POST':
        raisebugform = RaisebugForm(request.POST)
        if raisebugform.is_valid():
            f=raisebugform.save(commit=False)
            f.user=request.user
            f.save()

            return redirect('bugtrack/all_bugs.html')
    else:
        raisebugform = RaisebugForm()
    return render(request,'bugtrack/raisebug.html',context={'raisebugform': raisebugform })

def update_bugs(request,pk=None):
    obj=Bugs.objects.get(id=pk)
    if request.method=='POST':
        editbugform = RaisebugForm(request.POST,instance=obj)
        if editbugform.is_valid():
            editbugform.save()

            return redirect('bugtrack/all_bugs.html')
    else:
        editbugform = RaisebugForm(instance=obj)
    return render(request,'bugtrack/editbug.html',context={'editbugform': editbugform ,'pk':pk})

