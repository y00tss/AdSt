from django.urls import path
from django.urls.conf import include
from documentation import views as documentation_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', documentation_views.DocumentationView, basename='documentation')

urlpatterns = router.urls
