from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import TodoList
from .forms import TodoForm

def todo_list(request):
    todos = TodoList.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo add Successfully!')
            return HttpResponseRedirect(reverse('todo:home'))
    context = {
        'todos' : todos,
        'form'  : form
    } 
    return render(request, 'todo/index.html',context)

def todo_edit(request, pk):
    todo  = TodoList.objects.get(pk=pk)
    todos = TodoList.objects.all()
    form  = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Update Successfully!')
            return HttpResponseRedirect(reverse('todo:home'))
        
    context = {
        'todos' : todos,
        'form'  : form
    } 
    return render(request, 'todo/index.html',context)

def todo_delete(request, pk):
    todo  = TodoList.objects.get(pk=pk)
    todo.delete()
    messages.warning(request, 'Todo Delete Successfully!')
    return HttpResponseRedirect(reverse('todo:home'))
