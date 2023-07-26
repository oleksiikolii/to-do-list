from django.urls import path

from list_app.views import IndexView, TaskCreateView, TaskUpdateStateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path("task/create/", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>/update_state/", TaskUpdateStateView.as_view(), name="update-state"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task")
]

app_name = "list_app"
