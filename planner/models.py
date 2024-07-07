from django.db import models


class MonthlyCalendar(models.Model):
    current_month = models.IntegerField(default=1)

    def __str__(self):
        return str(self.current_month)


class TaskList(models.Model):
    task_date = models.DateField()
    monthly_calendar = models.ForeignKey(
        MonthlyCalendar, on_delete=models.CASCADE)
    task_amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.task_date)[:10]


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.name
