from django.db import models
from django.db.models import PROTECT
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

CHOISE_STATUS = [
    ("new", "новая"),
    ('in_progress', 'в процессе'),
    ('pending', 'ожидание'),
    ('blocked', 'заблокирована'),
    ('done', 'выполнена'),
]

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название категории")

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = CategoryManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_category_name')]

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()



class Task(models.Model):
    title = models.CharField(max_length=200, unique_for_date="created_at", verbose_name="Название задачи")
    description = models.TextField (verbose_name="Описание задачи")
    categories = models.ManyToManyField(Category, related_name='tasks', verbose_name='Категория задачи')
    status = models.CharField(max_length=15, choices=CHOISE_STATUS, verbose_name="Статус задачи")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task', default=1)

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        constraints = [models.UniqueConstraint(fields=['title'], name='unique_task_title')]



    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название подзадачи")
    description = models.TextField(verbose_name="Описание подзадачи")
    task = models.ForeignKey(Task, on_delete=PROTECT, related_name='subtasks', verbose_name='Основная задача')
    status = models.CharField(max_length=20, choices=CHOISE_STATUS, verbose_name="Статус подзадачи")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtask', default=1)

    class Meta:
        db_table = 'tasks_manager_subtask'
        ordering = ['-created_at']
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        constraints = [models.UniqueConstraint(fields=['title'], name='unique_subtask_title')]

    def __str__(self):
        return self.title

