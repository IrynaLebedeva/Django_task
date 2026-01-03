from django.apps import AppConfig


class TaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager'

    def ready(self):
        # print('task_manager signals loading')
        import task_manager.signals.task
