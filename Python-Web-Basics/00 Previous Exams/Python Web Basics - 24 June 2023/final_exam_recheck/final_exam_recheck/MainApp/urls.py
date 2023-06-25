from django.urls import path
from final_exam_recheck.MainApp.views import index, dashboard

urlpatterns = [
    path('', index, name='home page'),
    path('dashboard/', dashboard, name='dashboard page'),
]
