from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import listItem
from .forms import addItem
from django.contrib.auth.models import User

import datetime
# Create your views here.

def getBag(request):
    items = listItem.objects.all().order_by('date')
    return render(request, 'home.html', {'all_items': items})


def addToList(request):

    if request.method =='POST':
        form = addItem(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            q = form.cleaned_data['quantity']
            u = form.cleaned_data['unit']
            s = form.cleaned_data['status']
            d = form.cleaned_data['date']
            item = listItem(user_email=request.user.email, name=n, quantity=q, unit=u, status=s, date=d)
            item.save()
            
            #form.save()
            #print('Form is correct!')
            return HttpResponseRedirect('/getBag/')
        #else:
            #print('Form is invalid!!')
    
    form = addItem()
    return render(request, 'add.html', {'form': form})

def updateList(request, item_id):
    item = listItem.objects.get(id=item_id)
    form = addItem(instance=item)

    if request.method =='POST':
        update_form = addItem(request.POST, instance=item)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect('/getBag/')

    return render(request, 'add.html', {'form': form})#, 'item_id': item_id})


def deleteFromList(request, item_id):
    retrieve_item = listItem.objects.get(id=item_id)
    retrieve_item.delete()
    return HttpResponseRedirect('/getBag/')


def displayItem(request, item_id):
    item = listItem.objects.get(id=item_id)
    return render(request, 'list.html', {'item': item})

def searchbar(request):
    if request.method == 'GET':
        query_date = request.GET.get('search')
        try:
            items = listItem.objects.all().filter(date=query_date)
        except:
            items = listItem.objects.all()
        return render(request, 'home.html', {'all_items': items})