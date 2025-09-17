from django.shortcuts import render
from .models import Libros as Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'Libros/item_list.html', {'items': items})
