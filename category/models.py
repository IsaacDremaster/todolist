from django.db import models
from django.conf import settings

from user.models import Users


class Categories(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=300)
    description = models.TextField('Описание')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'category_user', null=True)

    def __str__(self):
        return self.name