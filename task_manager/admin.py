from django.contrib import admin
from .models import Task, SubTask, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "deadline", "created_at")
    search_fields = ('title',)
    list_filter = ('status','title')
    ordering = ('-created_at',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "task", "status", "deadline", "created_at")
    search_fields = ("title", "status")
    list_filter = ("title", "deadline" )
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Category)

