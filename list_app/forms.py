from django import forms

from list_app.models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(format='%d/%m/%Y %H:%M'),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
