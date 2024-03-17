from django.shortcuts import render,HttpResponse
from app1.models import RForm
from app1.form import RegForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
# Create your views here.
def reg(request):
    if request.method=='GET':
        var=RegForm()
        return render(request,'rg.html',{'var':var})
    elif request.method=='POST':
        form=RegForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.password=make_password(form.password)
            form.save()
            return HttpResponse('Your data has been saved')
        return HttpResponse('form is invalid')
    return HttpResponse('invalid')
def update(request,pk):
    a=RForm.objects.get(id=pk)
    if request.method=='GET':
        var=RegForm(instance=a)
        return render(request,'rg.html',{'var':var})
    elif request.method=='POST' and request.FILES:
        form=RegForm(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form=form.save(commit=False)
            p=form.password
            enc=make_password(p)
            form.password=enc
            form.save()
            return HttpResponse('Your data has been saved')
def read(request):
    var=RForm.objects.all()
    return render(request,'rd.html',{'var':var})
def delete():
    RForm.objects.all().delete()
    return HttpResponse('All data has been cleared')
def log(request):
    if request.method=='GET':
        var=AuthenticationForm()
        return render(request,'lg.html',{'var':var})
    elif request.method=='POST':
        user=request.POST['username']
        pw=request.POST['password']
        i=RForm.objects.get(username=user)
        v = authenticate(username=user,password=pw)
        if v is not None:
            return render(request,'hm.html',{'var':user,'var1':pw,'var2':i})
        else:
            return HttpResponse('Wrong username or password')