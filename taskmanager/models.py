from django.db import models
from django.utils import timezone
from django.conf import settings
import logging
# from django.contrib.auth.models import Group, User
from django_extensions.db import models as ext_models

logger = logging.getLogger(__name__)

class TaskStatus(models.Model):

    status = models.CharField(max_length=150, help_text="Статус задачи")

    def __str__(self) -> str:
        return f'{self.status}'

    class Meta:
        verbose_name_plural = 'Task statuses'

class Task(ext_models.TimeStampedModel):
    
    name = models.CharField(max_length=250, help_text="Описание задачи")
    is_active = models.BooleanField(default=True, help_text="Отметка о состоянии задачи")
    dead_line = models.DateField(
        default=None,
        null=True,
        help_text="Дата, до которой должна быть выполнена задача"
    )
    complete_time = models.DateTimeField(
        default=None,
        auto_now=False,
        blank=True,
        null=True,
        help_text="Время завершения задачи"
    )
    status = models.ForeignKey(
        to=TaskStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tasks_status',
        help_text='Статус',
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tasks_user',
        help_text='Исполнитель',
    )
    parent_task = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='sprint',
        help_text='Родительская категория спринт'
    )

    def save(self, *args, **kwargs) -> None:
        logger.warning(f'Save task "{self.name}"')
        if self.is_active and self.complete_time:
            self.complete_time = None
        elif not self.is_active and self.complete_time is None:
            self.complete_time = timezone.now()#.strftime("%d.%m.%Y")
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name} | deadline {self.dead_line.strftime("%d.%m.%Y")}'
    
    class Meta:
        ordering = ["created"]