from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..apis.viewsets import SnippetViewSet

router = DefaultRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]