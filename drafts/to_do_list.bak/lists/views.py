from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from lists.models import Item, List
# Create your views here.
def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect(resolve_url('home'))

    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, "lists/list.html", {'list': list_})

def new_list(request, list_id):
    list_ = List.objects.getid=list_id()
    Item.objects.filter(list=list_)
    return redirect(resolve_url('new_item', list_id=list_.id))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST.get('item_text'), list=list_)
    return redirect(resolve_url('view_list', list_id=list_id))
