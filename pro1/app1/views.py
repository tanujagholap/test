from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import Order


def create_view(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/create.html', {'form': form})


def show_view(request):
    obj = Order.objects.all()
    return render(request, 'app1/show.html', {'form': obj})


def update_view(request, pk):
    obj = Order.objects.get(id=pk)
    form = CreateForm(instance=obj)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/create.html', {'form': form})


def delete_view(request, pk):
    obj = Order.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'app1/confirm.html')
