from django.contrib import admin

from djangointroduction.todo_app.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass