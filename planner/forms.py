from django.forms import ModelForm, CheckboxInput, TextInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'new_task'})
        }
        labels = {
            'name': ""
        }


class TaskStateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['state']
        widgets = {
            'state': CheckboxInput(attrs={'onclick': 'this.form.submit();'})
        }
