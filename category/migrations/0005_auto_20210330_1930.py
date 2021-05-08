# Generated by Django 3.1.7 on 2021-03-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20210324_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(choices=[('None', None), ('HW', 'Homework'), ('JB', 'Job'), ('SC', 'School'), ('TD', 'ToDo'), ('TB', 'To buy')], default=1, max_length=300),
        ),
    ]