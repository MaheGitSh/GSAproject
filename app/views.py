from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Task
from django.views.decorators.http import require_POST


from.forms import TaskForm





def index(request):
    task = Task.objects.all()
    return render(request, 'accounts/index.html', {'task': task})

def add_tender(request):
    form=TaskForm()
    if request.method=='POST':
        # print(request.POST)
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contex={'form':form}
    return render(request, 'accounts/add_tender.html',contex)
    

def edit_tender(request, pk):
    tender=Task.objects.get(id=pk)
    form=TaskForm(instance=tender)
    contex={'form':form}
    if request.method=='POST':
        form=TaskForm(request.POST,instance=tender)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/add_tender.html',contex)


def delete_tender(request, pk):
    tender=Task.objects.get(id=pk)
    if request.method == 'POST':
        tender.delete()
        return redirect('/')
    contex={'item':tender}
    return render(request, 'accounts/delete_tender.html',contex)

def view_tender(request, pk):
    tender=Task.objects.get(id=pk)
    form=TaskForm(instance=tender)
    contex={'form':form}
    if request.method=='POST':
        form=TaskForm(request.POST,instance=tender)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/view_tender.html',contex)