from django.views import generic as views
from rest_framework import generics as api_views, serializers, permissions
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination

from django_rest_lab.api.models import Author


class ApiLoginVIew(ObtainAuthToken):
    ...


# # Create your views here.
# @api_view
# def rest_view(request):
#     ...

class AuthorGenericView(views.ListView):
    queryset = Author.objects.all()
    template_name = 'authors.html'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorsApiView(api_views.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorsApiViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'


class AuthorsApiCreateView(api_views.ListCreateAPIView):
    queryset = Author.objects.order_by('first_name', 'last_name', 'followers_count', 'pk')
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        request.session['count'] = 5

        return super().get(request, *args, **kwargs)
