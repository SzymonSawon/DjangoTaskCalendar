# Generated by Django 4.2.11 on 2024-07-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task_date',
            field=models.DateField(),
        ),
    ]
