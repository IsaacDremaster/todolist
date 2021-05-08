# Generated by Django 3.1.7 on 2021-04-16 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20210416_2014'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_tasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_task', to='category.categories'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_user', to=settings.AUTH_USER_MODEL),
        ),
    ]