from django.urls import path
from class_based_views_exercise.WebCBV.views import IndexView, some_test, TemplateView, RedirectView, ListView, \
    DetailsView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('test/', some_test, name='test page'),
    path('', IndexView.as_view(), name='base view'),
    path('template/', TemplateView.as_view(), name='template view'),
    path('redirect/', RedirectView.as_view(), name='redirect view'),
    path('listview/', ListView.as_view(), name='list view'),
    path('details/<int:pk>/', DetailsView.as_view(), name='details view'),
    path('create/', CreateView.as_view(), name='create view'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update view'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete view'),

]
