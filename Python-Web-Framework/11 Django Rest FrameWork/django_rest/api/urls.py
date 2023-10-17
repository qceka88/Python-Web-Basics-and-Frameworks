from django.urls import path
from rest_framework.routers import DefaultRouter

from django_rest_lab.api.views import AuthorGenericView, AuthorsApiCreateView, AuthorsApiViewSet

router = DefaultRouter()

router.register('author-vs', AuthorsApiViewSet, basename='author')

urlpatterns = [
    # *router.urls,
    path('authors/', AuthorsApiCreateView.as_view(), name='api list authors'),
    path('authors-ssr/', AuthorGenericView.as_view(), name='list generic view'),
    path('author-vs/', AuthorsApiViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    ))
]
