# Generated by Django 3.1.7 on 2021-03-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_categories_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.IntegerField(choices=[('1', None), ('2', 'Homework'), ('3', 'Job'), ('4', 'School'), ('5', 'ToDo'), ('6', 'To buy')], default=1),
        ),
    ]