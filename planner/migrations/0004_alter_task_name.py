# Generated by Django 4.2.11 on 2024-07-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_alter_task_deadline_alter_task_name_alter_task_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='defa', max_length=200),
            preserve_default=False,
        ),
    ]
