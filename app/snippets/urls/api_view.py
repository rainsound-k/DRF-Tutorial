from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis import api_view

urlpatterns = [
    path('', api_view.SnippetList.as_view()),
    path('<int:pk>/', api_view.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
