from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from list_app.forms import TaskForm
from list_app.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "list_app/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:homepage")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:homepage")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list_app/task_confirm_delete.html"
    success_url = reverse_lazy("list:homepage")


class TaskUpdateStateView(generic.View):
    def get(self, request, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.done = not task.done
        task.save()
        return redirect(reverse("list:homepage"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "list_app/tag_confirm_delete.html"
    success_url = reverse_lazy("list:tags")
