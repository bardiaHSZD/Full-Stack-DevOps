from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViews(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemViews(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer