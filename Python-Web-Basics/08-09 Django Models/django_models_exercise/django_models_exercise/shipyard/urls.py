from django.urls import path, include
from django_models_exercise.shipyard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.worker_details, name='view details'),
    path('delete/<int:pk>/', views.delete_worker, name='delete worker'),
    path('departments/', include([
        path('', views.departments_index, name='departments'),
        path('<slug:slug>/', views.department_details, name='department details'),
    ])),
    path('address/', include([
        path('', views.address_book, name='addresses'),
        path('<slug:slug>/', views.address_details, name='address details')])),

]
