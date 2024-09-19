from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemViews.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemViews.as_view()),
]