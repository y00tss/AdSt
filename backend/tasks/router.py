from django.urls import path
from django.urls.conf import include
from tasks import views as task_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", task_views.TaskViewSet, basename="tasks")
router.register(r"", task_views.TaskStatusChangeViewSet, basename="task-status")

urlpatterns = router.urls
