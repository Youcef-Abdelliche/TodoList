from django.contrib import admin
from .models import TodoList


class TodoAdmin(admin.ModelAdmin):
    fieldsets = ['Item Text:', {'fields': ['text']}
]


admin.site.register(TodoList)
