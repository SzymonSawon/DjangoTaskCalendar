from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_list_id>/", views.day_tasks, name="day_tasks"),
    path("<int:task_list_id>/create/", views.create_task, name="create_task"),
    path("<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("<int:task_id>/complete/", views.complete_task, name="complete_task"),
]
