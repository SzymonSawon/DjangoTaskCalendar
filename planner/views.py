from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskList, Task, MonthlyCalendar
from .forms import TaskForm, TaskStateForm
from datetime import date

import logging
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}


def index(request):
    dates = TaskList.objects.order_by("task_date")
    context = {
        "dates": dates,
    }

    logger = logging.getLogger('django')

    if not MonthlyCalendar.objects.exists():
        MonthlyCalendar.objects.create()
    monthly_calendar = MonthlyCalendar.objects.first()

    logger.info(f"{monthly_calendar.current_month}")
    logger.info(f"\n{date.today().month}")
    if monthly_calendar.current_month != date.today().month:
        logger.info("check1")
        monthly_calendar.current_month = date.today().month
        monthly_calendar.save()
        month_length = (date(date.today().year, date.today().month+1, 1) -
                        date(date.today().year, date.today().month, 1)).days
        logger.info("check2")
        logger.info(f"{month_length}")
        TaskList.objects.delete()
        for i in range(1, month_length+1):
            logger.info("check3")
            task_date = date(date.today().year, date.today().month, i)
            TaskList.objects.create(
                task_date=task_date, monthly_calendar=monthly_calendar)

    return render(request, "planner/index.html", context)


def day_tasks(request, task_list_id):
    form = TaskForm(request.POST or None)
    today = get_object_or_404(TaskList, pk=task_list_id)
    return render(request, "planner/day_tasks.html", {"today": today, "form": form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_list_id = task.task_list.id
    task.delete()
    today = get_object_or_404(TaskList, pk=task_list_id)
    today.task_amount -= 1
    today.save()
    return redirect("day_tasks", task_list_id=task_list_id)


def create_task(request, task_list_id):
    form = TaskForm(request.POST or None)
    today = get_object_or_404(TaskList, pk=task_list_id)
    today.task_amount += 1
    today.save()
    if form.is_valid():
        task_form = form.save(commit=False)
        task_form.task_list = today
        task_form.save()
    return redirect("day_tasks", task_list_id=task_list_id)


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_list_id = task.task_list.id
    task.state = True
    return redirect("day_tasks", task_list_id=task_list_id)
