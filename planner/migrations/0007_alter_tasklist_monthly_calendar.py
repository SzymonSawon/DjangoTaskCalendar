# Generated by Django 4.2.11 on 2024-07-04 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_monthlycalendar_tasklist_monthly_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='monthly_calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.monthlycalendar'),
        ),
    ]
