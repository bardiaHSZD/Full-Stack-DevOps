from django.contrib import admin
from .models import Logger
from .models import Reservations

# Register your models here.
admin.site.register(Logger)

admin.site.register(Reservations)
