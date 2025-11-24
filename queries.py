import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from task_manager.models import Task,SubTask, Category
from datetime import timedelta
from django.utils import timezone

new_task = Task.objects.create(
title="Prepare presentation",
description="Prepare materials and slides for the presentation",
status="New",
deadline=timezone.now()+timedelta(days=3)
)
print(new_task.id)

new_subtask_1 = SubTask.objects.create(
title="Gather information",
description="Find necessary information for the presentation",
status="New",
deadline=timezone.now()+timedelta(days=2),
task=new_task
)
print(new_subtask_1.id)

new_subtask_2 = SubTask.objects.create(
title="Create slides",
description="Create presentation slides",
status="New",
deadline=timezone.now()+timedelta(days=1),
task=new_task
)
print(new_subtask_2.id)
"""
Tasks со статусом "New":
Вывести все задачи, у которых статус "New".
"""


for task in Task.objects.filter(status="new"):
    print(task.title, task.status)


"""
SubTasks с просроченным статусом "Done":
Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.
"""


for subtask in SubTask.objects.filter(status="done", deadline__lt=timezone.now()):
    print(subtask.title, subtask.status)



# Измените статус "Prepare presentation" на "In progress".

n_status = Task.objects.get(title="Prepare presentation")
n_status.status = "In progress"
n_status.save()

# Измените срок выполнения для "Gather information" на два дня назад.

n_subtask_1 = SubTask.objects.get(title="Gather information")
n_subtask_1.deadline = n_subtask_1.deadline - timedelta(days=2)
n_subtask_1.save()

# Измените описание для "Create slides" на "Create and format presentation slides".

n_subtask_2 = SubTask.objects.get(title="Create slides")
n_subtask_2.description = "Create and format presentation slides"
n_subtask_2.save()

# Удалите задачу "Prepare presentation" и все ее подзадачи

task_3 = Task.objects.get(title="Prepare presentation")
task_3.subtasks.all().delete()
task_3.delete()


