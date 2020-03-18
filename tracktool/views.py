from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from .models import Bugs
from .forms import RaisebugForm

# Create your views here.
def home(requset):
    return render(requset,'bugtrack/home.html',context={})

@login_required(login_url='accounts_urls:userloginpage')
def all_bugs(request):
    bugs=Bugs.objects.all()
    return render (request,'bugtrack/all_bugs.html',context={'bugs':bugs })
#
@login_required(login_url='accounts_urls:userloginpage')
def raise_bugs(request):
    if request.method=='POST':
        raisebugform = RaisebugForm(request.POST)
        if raisebugform.is_valid():
            f=raisebugform.save(commit=False)
            f.user=request.user
            f.save()

            return redirect('tracktool_urls:my_bugs')
    else:
        raisebugform = RaisebugForm()
    return render(request,'bugtrack/raisebug.html',context={'raisebugform': raisebugform })

def update_request(request,pk=None):
    obj=Bugs.objects.get(pk=pk)
    if request.method=='POST':
        editbugform = RaisebugForm(request.POST,instance=obj)
        if editbugform.is_valid():
            editbugform.save()

            return redirect('tracktool_urls:my_bugs')
    else:
        editbugform = RaisebugForm(instance=obj)
    return render(request,'bugtrack/editbug.html',context={'editbugform': editbugform ,'pk':pk})
#
# def delete_request(request,pk=None):
#     obj=Bugs.objects.get(pk=pk)
#     obj.delete()
#     return redirect('bugtrack/all_bugs.html')


def my_bugs(request):
    bugs = Bugs.objects.filter(name=request.user,)
    return render(request, 'bugtrack/my_bugs.html', context={'bugs': bugs,})

