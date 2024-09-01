from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_items = MenuItemSerializer(items, many = True)
        return Response(serialized_items.data)
    if request.method == 'POST':
        serialized_items = MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_items = MenuItemSerializer(items)
    return Response(serialized_items.data)