from django.shortcuts import render
from django.urls import reverse
from .models import TodoList
from django.http import HttpResponseRedirect


def home(request):
    items_list = TodoList.objects.all().order_by('-added_date')
    return render(request, 'index.html', {'items_list': items_list})


def add_todo(request):
    item_text = request.POST.get('add_item')
    TodoList.objects.create(text=item_text)
    return HttpResponseRedirect('/')


