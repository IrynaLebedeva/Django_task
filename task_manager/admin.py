from django.contrib import admin
from .models import Task, SubTask, Category


class SubTaskInlineAdmin(admin.TabularInline):
    model = SubTask
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("short_title", "description", "status", "deadline", "created_at")
    search_fields = ('title',)
    list_filter = ('status','title')
    ordering = ('-created_at',)
    inlines = [SubTaskInlineAdmin]

    def short_title(self, obj):
        if len(obj.title) >10:
            return obj.title[:10]+"..."
        return obj.title
    short_title.short_description = 'Title'


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "task", "status", "deadline", "created_at")
    search_fields = ("title", "status")
    list_filter = ("title", "deadline" )
    ordering = ('-created_at',)

    @admin.action(description="Mark Subtasks as Done")
    def mark_done(self, request, queryset):
        queryset.update(status="done")

    actions = ["mark_done"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Category)

