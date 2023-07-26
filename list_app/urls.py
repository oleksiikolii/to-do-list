from django.urls import path

from list_app.views import (
    IndexView,
    TaskCreateView,
    TaskUpdateStateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path("tag/", TagListView.as_view(), name="tags"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>/update_state/", TaskUpdateStateView.as_view(), name="update-state"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task")
]

app_name = "list_app"
