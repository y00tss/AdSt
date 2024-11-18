from django.urls import path
from django.urls.conf import include
from groups import views as groups_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', groups_views.GroupsView, basename='groups')

urlpatterns = router.urls
