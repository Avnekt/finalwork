from django.contrib import admin
from taskmanager.models import Task, TaskStatus
from django.db import models
from django.utils import timezone

@admin.action(description="Cancel task finish")
def cancel_complete(self, request, queryset: models.QuerySet):
    queryset.update(is_active=True, complete_time=None)

@admin.action(description="Task finished")
def make_complete(self, request, queryset: models.QuerySet):
    queryset.update(is_active=False, complete_time=timezone.now())

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    
    list_display = [
        "id",
        "name",
        "is_active",
        "dead_line",
        "status"
    ]

    actions = [
        cancel_complete,
        make_complete
    ]

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):

    list_display = [
        'status'
    ]
