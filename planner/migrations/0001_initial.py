# Generated by Django 4.2.11 on 2024-07-03 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_date', models.DateTimeField(verbose_name='task_date')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField(verbose_name='start')),
                ('deadline', models.DateTimeField(verbose_name='deadline')),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.tasklist')),
            ],
        ),
    ]