from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_items = MenuItemSerializer(items, many = True)
    return Response(serialized_items.data)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_items = MenuItemSerializer(items)
    return Response(serialized_items.data)