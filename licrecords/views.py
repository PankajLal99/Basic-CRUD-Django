from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def home(request):
    form=forms.customerform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context={
        'form':form
    }
    return render(request,'licrecords/home.html',context)

def view(request):
    cust=models.Cutomer.objects.all()
    context={
        'customer':cust
    }
    return render(request,'licrecords/view.html',context)

def delete(request,pk):
    models.Cutomer.objects.get(id=pk).delete()
    return redirect('home')

def edit(request,pk):
    cust=models.Cutomer.objects.get(id=pk)
    form=forms.customerform(request.POST or None,instance=cust,initial={"name":cust.name})
    if form.is_valid():
        form.save()
        return redirect('view')
    context={
        'form':form
    }
    return render(request,'licrecords/home.html',context)