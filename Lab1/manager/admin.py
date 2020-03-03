from django.contrib import admin

from manager.models import Task


class TaskAdmin(admin.ModelAdmin):
    exclude = ()


admin.site.register(Task, TaskAdmin)