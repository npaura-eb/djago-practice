from django.contrib import admin
from .models import Priority, Todo
# Register your models here.

admin.site.register(Todo)
admin.site.register(Priority)

