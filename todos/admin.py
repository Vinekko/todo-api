from django.contrib import admin
from .models import todoItem

# Register your models here.

class todoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'completed', 'created', 'updated']
    list_filter = ['completed', 'created']
    search_fields = ['title']

admin.site.register(todoItem, todoItemAdmin)