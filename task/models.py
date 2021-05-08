from django.db import models
from django.conf import settings

from category.models import Categories


class Tasks(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    description = models.TextField('Описание')
    deadline = models.DateTimeField('Дэд лайн', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'tasks_user', null=True)
    category = models.ForeignKey('category.Categories', models.CASCADE, 'category_task', null=True)

    def __str__(self):
        return self.title
