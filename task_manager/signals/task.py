from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from task_manager.models import Task


@receiver(pre_save, sender=Task)
def task_pre_save(sender, instance, **kwargs):
    if instance.pk:
        instance._old_status = Task.objects.get(pk=instance.pk).status
    else:
        instance._old_status = None


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        # print('объект только что создан')
        return
    # print(f'old_status={instance._old_status}, new_status={instance.status}')

    if instance._old_status == instance.status:
        # print('статус не изменился')
        return
    # print('статус изменился - отправляем email')

    if not instance.owner.email:
        # print('нет email')
        return
    send_mail(
        subject=f'Статус задачи изменён: {instance.title}',
        message=(
            f'Здравствуйте, {instance.owner.username}!\n\n'
            f'Статус задачи изменился с '
            f'"{instance._old_status}" на "{instance.status}".'
        ),
        from_email=None,
        recipient_list=[instance.owner.email],
    )


